import json
from channels.generic.websocket import AsyncWebsocketConsumer

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import PrivateMessage
from django.contrib.auth.models import User


class PrivateChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Lấy user từ scope
        self.user = self.scope['user']
        self.other_user_id = self.scope['url_route']['kwargs']['user_id']

        # Tạo tên phòng chung
        self.room_name = f"private_chat_{min(self.user.id, int(self.other_user_id))}_{max(self.user.id, int(self.other_user_id))}"

        # Thêm vào group (phòng chat)
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Rời group khi ngắt kết nối
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Nhận tin nhắn từ WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Lưu tin nhắn vào cơ sở dữ liệu
        receiver = User.objects.get(id=self.other_user_id)
        PrivateMessage.objects.create(
            sender=self.user,
            receiver=receiver,
            content=message
        )

        # Gửi tin nhắn tới group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.user.username
            }
        )

    async def chat_message(self, event):
        # Gửi tin nhắn cho WebSocket client
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'sender': event['sender']
        }))