from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PrivateMessage
from .serializers import PrivateMessageSerializer

@api_view(['GET'])
@csrf_exempt
def get_private_messages(request, user_id):
    user_info = check_user_session()
    print(user_info)
    if not user_info:
        return Response({"error": "User not u authenticated."}, status=599)

    # Tiến hành lấy tin nhắn cho người dùng đã xác thực
    messages = PrivateMessage.objects.filter(
        sender_id=user_info['id'], receiver_id=user_id
    )

    # Sử dụng serializer để chuyển dữ liệu thành JSON
    serializer = PrivateMessageSerializer(messages, many=True)

    return Response({"messages": serializer.data})

import requests

def check_user_session():
    try:
        # Gửi yêu cầu đến User Service để kiểm tra session
        response = requests.get('http://127.0.0.1:8000/users/get_session_status/',)
        print(response.status_code)
        print(response.json())
        # Kiểm tra nếu phản hồi thành công
        if response.status_code == 200:
            data = response.json()
            # Kiểm tra xem người dùng có xác thực hay không
            if data.get('is_authenticated', False):
                return data  # Trả về thông tin người dùng
    except requests.exceptions.RequestException as e:
        # Xử lý ngoại lệ nếu có lỗi trong quá trình gửi yêu cầu (ví dụ: không thể kết nối tới dịch vụ)
        print(f"Error while checking session: {e}")

    return False  # Trả về False nếu không xác thực hoặc có lỗi xảy ra