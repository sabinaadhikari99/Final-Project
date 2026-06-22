from django.urls import path
from django.views.generic import TemplateView

app_name = 'recommendations'

urlpatterns = [
    path("job/", TemplateView.as_view(template_name="recommendations.html"), name="job"),
    path("ai-match/", TemplateView.as_view(template_name="recommendations.html"), name="ai-match"),
]