from django.urls import path
from . import views
from .views import list_users

urlpatterns = [
    path('register/', views.register_user, name='register'),
    # Các URL khác
    path('login/', views.login_user, name='login'),
    path('users/', list_users, name='list_users'),
]
