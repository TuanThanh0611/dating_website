from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    # Các URL khác
    path('login/', views.login_user, name='login'),
]
