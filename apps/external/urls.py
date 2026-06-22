from django.urls import path
from django.views.generic import TemplateView
from .views import LinkedInJobsAPIView

app_name = 'external'

urlpatterns = [
    path("linkedin/", TemplateView.as_view(template_name="linkedin.html"), name="linkedin"),
    path("linkedin/", LinkedInJobsAPIView.as_view(), name="api-linkedin"),
]