from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
from .services import UserService


@csrf_exempt
def update_username(request, user_id):
    """
    Xử lý cập nhật username qua HTTP POST request.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            new_username = data.get("username")
            if not new_username:
                raise ValueError("Username is required")
            user = UserService.update_username(user_id, new_username)
            return JsonResponse({"success": True, "username": user.username}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)
        except ValueError as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)


@csrf_exempt
def update_email(request, user_id):
    """
    Xử lý cập nhật email qua HTTP POST request.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            new_email = data.get("email")
            if not new_email:
                raise ValueError("Email is required")
            user = UserService.update_email(user_id, new_email)
            return JsonResponse({"success": True, "email": user.email}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)
        except ValueError as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)


@csrf_exempt
def update_first_name(request, user_id):
    """
    Xử lý cập nhật first name qua HTTP POST request.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            first_name = data.get("first_name")
            if not first_name:
                raise ValueError("First name is required")
            user = UserService.update_first_name(user_id, first_name)
            return JsonResponse({"success": True, "first_name": user.first_name}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)
        except ValueError as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)


@csrf_exempt
def update_last_name(request, user_id):
    """
    Xử lý cập nhật last name qua HTTP POST request.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            last_name = data.get("last_name")
            if not last_name:
                raise ValueError("Last name is required")
            user = UserService.update_last_name(user_id, last_name)
            return JsonResponse({"success": True, "last_name": user.last_name}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)
        except ValueError as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)


@csrf_exempt
def update_phone_number(request, user_id):
    """
    Xử lý cập nhật số điện thoại qua HTTP POST request.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            phone_number = data.get("phone_number")
            if not phone_number:
                raise ValueError("Phone number is required")
            user = UserService.update_phone_number(user_id, phone_number)
            return JsonResponse({"success": True, "phone_number": user.phone_number}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)
        except ValueError as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)


@csrf_exempt
def update_password(request, user_id):
    """
    Xử lý cập nhật mật khẩu qua HTTP POST request.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            new_password = data.get("password")
            if not new_password:
                raise ValueError("Password is required")
            UserService.update_password(user_id, new_password)
            return JsonResponse({"success": True, "message": "Password updated successfully"}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)
        except ValueError as e:
            return JsonResponse({"success": False, "error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)


@csrf_exempt
def deactivate_user(request, user_id):
    """
    Xử lý vô hiệu hóa người dùng qua HTTP POST request.
    """
    if request.method == "POST":
        try:
            UserService.deactivate_user(user_id)
            return JsonResponse({"success": True, "message": "User deactivated successfully"}, status=200)
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"}, status=404)
        except Exception as e:
            return JsonResponse({"success": False, "error": "An error occurred: " + str(e)}, status=500)

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)
from .models import User
@csrf_exempt
def list_users(request):
    """
    View để lấy danh sách tất cả người dùng.
    """
    if request.method == "GET":
        # Lấy tất cả user từ database
        users = User.objects.all()

        # Chuyển đổi dữ liệu người dùng thành JSON
        users_data = [
            {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": getattr(user, "phone_number", None),  # Nếu có field phone_number
                "is_active": user.is_active,
            }
            for user in users
        ]

        # Trả về dữ liệu dưới dạng JSON
        return JsonResponse({"success": True, "users": users_data}, status=200)

    # Nếu request không phải GET, trả về lỗi Method Not Allowed
    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)
