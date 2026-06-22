from django.urls import path
from django.views.generic import TemplateView
from .views import ChatbotAPIView, InterviewAPIView

app_name = 'chatbot'

urlpatterns = [
    path("", TemplateView.as_view(template_name="chat.html"), name="list"),
    path("", ChatbotAPIView.as_view(), name="api-chatbot"),
    path("interview/", InterviewAPIView.as_view(), name="api-interview"),
]