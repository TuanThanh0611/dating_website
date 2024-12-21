from django.urls import path
from . import views
from .views import list_users, get_session_status, logout_view,login_user,register_user

urlpatterns = [
    path('register/', register_user, name='register'),
    # Các URL khác
    path('login/', login_user, name='login'),
    path('users/', list_users, name='list_users'),
    path('get_session_status/', get_session_status, name='get_session_status'),
    path('logout/', logout_view, name='logout_view'),
]
