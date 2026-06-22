from django.urls import path
from django.views.generic import TemplateView
from .views import QuizAPIView, QuizSubmitAPIView

app_name = 'quiz'

urlpatterns = [
    path("", TemplateView.as_view(template_name="quiz.html"), name="list"),
    path("", QuizAPIView.as_view(), name="api-quiz"),
    path("submit/", QuizSubmitAPIView.as_view(), name="api-submit"),
]