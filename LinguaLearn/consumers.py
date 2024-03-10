from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging
import httpx
from django.conf import settings
from conf import GENERATIVE_PARAM

# from LinguaLearn.api import get_response_from_api

# Получение инстанса логгера
logger = logging.getLogger('django.channels')


# Функция для асинхронного запроса к API
# Функция для асинхронного запроса к API, теперь принимает отдельно сообщение и историю
async def get_response_from_api(message, history):
    logger.info(f'Вызов метода get {message} с историей {history}')
    api_url = f'http://127.0.0.1:8001/api/generative-response/' if GENERATIVE_PARAM else f'http://127.0.0.1:8000/api/response-lookup/'
    logger.info(f'Вызов {api_url}')
    json_data = {'new_question': message, 'history': history} if GENERATIVE_PARAM else {'new_question': message}
    async with httpx.AsyncClient() as client:
        # Отправляем и сообщение \ и историю
        response = await client.post(api_url, json=json_data)
        result = response.json()
    return result['response']


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_history = []

    async def connect(self):
        await self.accept()
        logger.info('WebSocket соединение установлено')

    async def disconnect(self, close_code):
        self.message_history.clear()
        logger.info(f'WebSocket соединение закрыто: {close_code}')

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        logger.info(f'Получено сообщение от {sender}: {message}')

        if sender == 'user':
            # Обновляем историю, сохраняя только 4 последних взаимодействия (вопрос-ответ)
            self.message_history.append(f"User: {message}")
            if len(self.message_history) > 8:
                self.message_history = self.message_history[-8:]
            logger.info(f'История диалога: {self.message_history}')
            # Преобразование истории в строку передается в аргументах отдельно
            history_str = " ".join(self.message_history[:-1])  # Последнее сообщение пользователя не включаем в историю
            await self.process_user_message(message, history_str)

    async def process_user_message(self, message, history_str):
        # Получение ответа от API, теперь передаем историю как отдельный параметр
        response = await get_response_from_api(message, history_str)
        logger.info(f'Обработка сообщения {message}')
        # Добавляем ответ бота в историю
        self.message_history.append(f"Bot: {response}")
        # Отправка ответа от бота клиенту через WebSocket
        await self.send_bot_message(response)

    async def send_bot_message(self, message):
        logger.info(f'Отправка ответа от бота: {message}')
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': 'bot'
        }))
