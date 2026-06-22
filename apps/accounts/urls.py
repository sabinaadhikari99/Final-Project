from django.urls import path
from django.views.generic import TemplateView
from .views import LoginAPIView, ProfileAPIView, RegisterAPIView, ResumeUploadAPIView

app_name = 'accounts'

urlpatterns = [
    # ==================== FRONTEND ROUTES ====================
    path("", TemplateView.as_view(template_name="accounts/login.html"), name="home"),
    path("login/", TemplateView.as_view(template_name="accounts/login.html"), name="login"),
    path("register/", TemplateView.as_view(template_name="accounts/register.html"), name="register"),
    path("profile/settings/", TemplateView.as_view(template_name="accounts/profile_settings.html"), name="profile-settings"),
    
    # ==================== API ROUTES ====================
    path("register/", RegisterAPIView.as_view(), name="api-register"),
    path("login/", LoginAPIView.as_view(), name="api-login"),
    path("profile/", ProfileAPIView.as_view(), name="api-profile"),
    path("resume/", ResumeUploadAPIView.as_view(), name="api-resume"),
]