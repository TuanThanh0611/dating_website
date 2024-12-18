from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import User

class UserService:
    @staticmethod
    def update_username(user_id, new_username):
        user = User.objects.get(id=user_id)
        user.username = new_username
        user.save()
        return user

    @staticmethod
    def update_email(user_id, new_email):
        user = User.objects.get(id=user_id)
        user.email = new_email
        user.save()
        return user

    @staticmethod
    def update_first_name(user_id, first_name):
        user = User.objects.get(id=user_id)
        user.first_name = first_name
        user.save()
        return user

    @staticmethod
    def update_last_name(user_id, last_name):
        user = User.objects.get(id=user_id)
        user.last_name = last_name
        user.save()
        return user

    @staticmethod
    def update_phone_number(user_id, phone_number):
        user = User.objects.get(id=user_id)
        user.phone_number = phone_number
        user.save()
        return user

    @staticmethod
    def update_password(user_id, new_password):
        user = User.objects.get(id=user_id)
        user.password = make_password(new_password)  # Hash mật khẩu trước khi lưu
        user.save()
        return user

    @staticmethod
    def deactivate_user(user_id):
        user = User.objects.get(id=user_id)
        user.is_active = False
        user.save()
        return user


