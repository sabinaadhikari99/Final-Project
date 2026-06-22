from django.urls import path
from django.views.generic import TemplateView
from .views import NotificationListAPIView, NotificationMarkReadAPIView

app_name = 'notifications'

urlpatterns = [
    path("", TemplateView.as_view(template_name="notifications.html"), name="list"),
    path("", NotificationListAPIView.as_view(), name="api-list"),
    path("<int:pk>/read/", NotificationMarkReadAPIView.as_view(), name="api-read"),
]