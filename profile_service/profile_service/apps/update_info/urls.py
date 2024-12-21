from django.conf.urls.static import static
from django.urls import path
from .views import (
    update_username,
    update_email,
    update_first_name,
    update_last_name,
    update_phone_number,
    update_password,
    deactivate_user,
    list_users, UploadAvatarView,
)
from ... import settings

urlpatterns = [
    path('<int:user_id>/update-username/', update_username, name='update_username'),
    path('user/<int:user_id>/update-email/', update_email, name='update_email'),
    path('user/<int:user_id>/update-first-name/', update_first_name, name='update_first_name'),
    path('user/<int:user_id>/update-last-name/', update_last_name, name='update_last_name'),
    path('user/<int:user_id>/update-phone-number/', update_phone_number, name='update_phone_number'),
    path('user/<int:user_id>/update-password/', update_password, name='update_password'),
    path('<int:user_id>/deactivate/', deactivate_user, name='deactivate_user'),
    path('users/', list_users, name='list_users'),
    path('<int:user_id>/update-avatar/', UploadAvatarView.as_view(), name='upload_avatar'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)