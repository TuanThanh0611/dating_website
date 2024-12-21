

from django.urls import path
from .views import send_confirmation_email
urlpatterns = [
    path('send-confirmation-email/', send_confirmation_email, name='send_confirmation_email'),
]
