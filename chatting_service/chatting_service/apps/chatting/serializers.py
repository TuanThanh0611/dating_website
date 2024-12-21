
from rest_framework import serializers
from .models import PrivateMessage

class PrivateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateMessage
        fields = ['sender', 'receiver', 'content', 'timestamp']