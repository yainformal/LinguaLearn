# main_app/routing.py

from django.urls import path
from LinguaLearn import consumers

websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
]
