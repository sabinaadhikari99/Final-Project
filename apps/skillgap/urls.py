from django.urls import path
from django.views.generic import TemplateView
from .views import SkillGapAPIView

app_name = 'skillgap'

urlpatterns = [
    path("", TemplateView.as_view(template_name="skillgap.html"), name="list"),
    path("", SkillGapAPIView.as_view(), name="api-skillgap"),
]