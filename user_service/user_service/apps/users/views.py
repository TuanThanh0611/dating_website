from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from user_service.apps.users.services import UserService

# Create your views here.
@csrf_exempt
def register_user(request):
    """
    Xử lý đăng ký người dùng mới qua HTTP POST request.
    """
    if request.method == "POST":
        try:
            # Lấy dữ liệu từ request (thường là JSON)
            import json
            data = json.loads(request.body)

            # Gọi phương thức tạo người dùng
            user_data = UserService.create_user(data)

            # Trả về thông tin người dùng đã tạo thành công
            return JsonResponse({"success": True, "user": user_data}, status=201)

        except ValueError as e:
            # Trả về lỗi nếu thiếu trường hoặc lỗi khi tạo người dùng
            return JsonResponse({"success": False, "error": str(e)}, status=400)

        except Exception as e:
            # Trường hợp lỗi không xác định
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    # Nếu không phải POST request, trả về lỗi method not allowed
    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)


import json
from user_service.apps.users.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
import bcrypt
from user_service.apps.users.services import JWTService

@csrf_exempt
def login_user(request):

    if request.method == "POST":
        try:
            # Lấy dữ liệu từ request (thường là JSON)
            data = json.loads(request.body)

            email = data.get("email")
            password = data.get("password")

            if not email or not password:
                return JsonResponse({"success": False, "error": "Email and password are required."}, status=400)

            # Tìm người dùng theo email
            try:
                user = User.objects.get(email=email)  # Truy vấn trực tiếp từ model User
            except User.DoesNotExist:
                return JsonResponse({"success": False, "error": "Invalid credentials."}, status=401)

            # Kiểm tra mật khẩu
            if not check_password(password, user.password):  # Đảm bảo bạn sử dụng user.password, không phải user["password"]
                return JsonResponse({"success": False, "error": "Invalid credentials."}, status=401)

            # Tạo JWT token hoặc trả về thông tin người dùng
            token = JWTService.generate_token(user)

            return JsonResponse({"success": True, "token": token}, status=200)

        except ValueError as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)

        except Exception as e:
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    # Nếu không phải POST request, trả về lỗi method not allowed
    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)