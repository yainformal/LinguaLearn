from channels.generic.websocket import AsyncWebsocketConsumer
import json
import logging

# Получение инстанса логгера
logger = logging.getLogger('django.channels')

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        logger.info('WebSocket соединение установлено')

    async def disconnect(self, close_code):
        logger.info(f'WebSocket соединение закрыто: {close_code}')

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']
        logger.info(f'Получено сообщение от {sender}: {message}')

        if sender == 'user':
            await self.send_bot_message(message)

    async def send_bot_message(self, message):
        response = "Ответ от бота на ваше сообщение: " + message
        logger.info(f'Отправка ответа от бота: {response}')
        await self.send(text_data=json.dumps({
            'message': response,
            'sender': 'bot'
        }))
