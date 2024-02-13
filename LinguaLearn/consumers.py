from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = text_data_json['sender']

        if sender == 'user':
            await self.send_bot_message(message)

    async def send_bot_message(self, message):
        response = "Ответ от бота на ваше сообщение: " + message
        await self.send(text_data=json.dumps({
            'message': response,
            'sender': 'bot'
        }))
