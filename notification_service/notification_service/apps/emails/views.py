from datetime import datetime

from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
import random
import string
import json
from django.views.decorators.csrf import csrf_exempt


# Hàm tạo mã xác nhận ngẫu nhiên
def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# View gửi email xác nhận
from django.http import JsonResponse
@csrf_exempt
def send_confirmation_email(request):
    if request.method == 'POST':
        try:
            # Lấy dữ liệu JSON từ body
            data = json.loads(request.body)
            user_email = data.get('user_email')  # Lấy user_email từ body

            if not user_email:
                return JsonResponse({'status': 'error', 'message': 'Email không được cung cấp.'}, status=400)

            # Tạo mã xác nhận ngẫu nhiên
            confirmation_code = generate_confirmation_code()

            # Lưu mã vào session
            request.session['confirmation_code'] = confirmation_code
            request.session['confirmation_code_time'] = str(datetime.datetime.now())
            request.session['user_email'] = user_email

            # Gửi email
            subject = 'Xác nhận mã của bạn'
            message = f'Mã xác nhận của bạn là: {confirmation_code}'
            from_email = settings.EMAIL_HOST_USER

            send_mail(subject, message, from_email, [user_email])
            return JsonResponse({'status': 'success', 'message': 'Mã xác nhận đã được gửi.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Phương thức không được hỗ trợ.'}, status=405)

import datetime
from django.http import JsonResponse

def verify_confirmation_code(request, user_email, code):
    # Kiểm tra xem mã có tồn tại trong session không
    stored_code = request.session.get('confirmation_code')
    stored_time = request.session.get('confirmation_code_time')
    if not stored_code or stored_code != code:
        return JsonResponse({'status': 'error', 'message': 'Mã xác nhận không hợp lệ.'})

    # Kiểm tra thời gian hết hạn của mã
    if stored_time:
        time_diff = datetime.datetime.now() - datetime.datetime.strptime(stored_time, '%Y-%m-%d %H:%M:%S.%f')
        if time_diff.total_seconds() > 300:  # 300 giây = 5 phút
            return JsonResponse({'status': 'error', 'message': 'Mã xác nhận đã hết hạn.'})

    # Nếu mã hợp lệ và chưa hết hạn
    return JsonResponse({'status': 'success', 'message': 'Xác nhận thành công.'})