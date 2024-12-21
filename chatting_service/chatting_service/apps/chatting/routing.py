

from django.urls import path
from .consumers import PrivateChatConsumer

websocket_urlpatterns = [
    path('ws/private-chat/<int:user_id>/', PrivateChatConsumer.as_asgi()),
]