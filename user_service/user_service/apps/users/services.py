from django.db import IntegrityError
from .models import User
from django.contrib.auth.hashers import make_password
class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        """
        Lấy thông tin người dùng từ database.
        """
        try:
            user = User.objects.get(id=user_id)

            return {"id": user.id, "name": user.name, "email": user.email}
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user_by_email(user_email):
        try:
            # Tìm người dùng theo email
            user = User.objects.get(email=user_email)

            # Trả về đối tượng user, không phải là set
            return user  # Trả về đối tượng user
        except User.DoesNotExist:
            return None

    @staticmethod
    def create_user(data):
        """
        Tạo người dùng mới.
        """
        required_fields = ["username", "email", "password"]

        # Kiểm tra các trường bắt buộc
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"Missing required field: {field}")

        try:
            # Tạo người dùng mới
            user = User.objects.create(
                username=data["username"],
                email=data["email"],
                password=make_password(data["password"])  # Lưu ý: Cần mã hóa mật khẩu
            )
            return {"id": user.id, "username": user.username, "email": user.email}
        except IntegrityError:
            # Trường hợp email bị trùng hoặc lỗi database
            raise ValueError("A user with this email already exists.")

import jwt
from datetime import datetime, timedelta

class JWTService:
    # Khóa bí mật để ký JWT
    SIGNER_KEY = "Hvj3OStJfA9Ze823YyodKyYSJ33T555IRYFs2yIOcPLiP10J8pMj1wfy8zi2ZWAw"

    @staticmethod
    def generate_token(user):
        # Header của JWT
        header = {
            "alg": "HS512",  # Thuật toán ký
            "typ": "JWT"     # Định dạng
        }

        # Claims của JWT
        claims = {
            "sub": user.email,               # Định danh người dùng
            "iss": "ivo.com",                   # Nhà phát hành token
            "iat": datetime.utcnow(),           # Thời gian phát hành
            "exp": datetime.utcnow() + timedelta(hours=72),  # Thời gian hết hạn
            "scope": "user",                    # Thông tin bổ sung (phạm vi quyền)
            "id": user.id
        }

        token = jwt.encode(claims, JWTService.SIGNER_KEY, algorithm="HS512", headers=header)
        return token


