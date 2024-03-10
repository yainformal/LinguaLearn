from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging
import httpx
from django.conf import settings
from conf import GENERATIVE_PARAM

#from LinguaLearn.api import get_response_from_api

# Получение инстанса логгера
logger = logging.getLogger('django.channels')

# Функция для асинхронного запроса к API
async def get_response_from_api(message):
    logger.info(f'Вызов метода get {message}')
    if GENERATIVE_PARAM:
        api_url = f'http://127.0.0.1:8001/api/generative-response/'
    else:
        api_url = f'http://127.0.0.1:8000/api/response-lookup/'  # URL вашего API
    logger.info(f'Вызов {api_url}')
    async with httpx.AsyncClient() as client:
        response = await client.post(api_url, json={'new_question': message})
        result = response.json()
    return result['response']



class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_history = []
        self.history = None

    async def connect(self):
        await self.accept()
        self.message_history = []
        logger.info('WebSocket соединение установлено')

    async def disconnect(self, close_code):
        self.message_history = []
        logger.info(f'WebSocket соединение закрыто: {close_code}')

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        logger.info(f'Получено сообщение от {sender}: {message}')

        if sender == 'user':
            # Храним в контексте 4 последних сообщения 
            self.message_history.append(message)
            if len(self.message_history) > 4:
                self.message_history.pop(0)
            logger.info(f'{self.message_history}')
            history_str = " ".join(self.message_history)
            await self.process_user_message(history_str)

    async def process_user_message(self, message):
        # Получение ответа от API
        response = await get_response_from_api(message)
        logger.info(f'Обработка сообщения {message}')
        # Отправка ответа от бота клиенту через WebSocket
        await self.send_bot_message(response)

    async def send_bot_message(self, message):
        logger.info(f'Отправка ответа от бота: {message}')
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': 'bot'
        }))

