
from django.urls import path
from .views import get_private_messages


urlpatterns = [
    path('private-chat/<int:user_id>/', get_private_messages, name='private_chat_messages'),
]