from django.urls import path
from .views import (
    AdminReportsAPIView, AdminUserDetailAPIView, AdminUsersAPIView,
    SystemSettingDetailAPIView, SystemSettingsAPIView,
)

app_name = 'admin_panel'

urlpatterns = [
    path("users/", AdminUsersAPIView.as_view(), name="users"),
    path("users/<int:pk>/", AdminUserDetailAPIView.as_view(), name="user-detail"),
    path("reports/", AdminReportsAPIView.as_view(), name="reports"),
    path("settings/", SystemSettingsAPIView.as_view(), name="settings"),
    path("settings/<int:pk>/", SystemSettingDetailAPIView.as_view(), name="setting-detail"),
]