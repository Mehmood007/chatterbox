from django.urls import path
from webchat.consumer import WebChatConsumer

websocket_urlpatterns = [
    path('<str:serverId>/<str:channelId>', WebChatConsumer.as_asgi())
]
