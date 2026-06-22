from django.urls import path
from django.views.generic import TemplateView

app_name = 'dashboard'

urlpatterns = [
    path("seeker/", TemplateView.as_view(template_name="dashboard/seeker.html"), name="seeker"),
    path("recruiter/", TemplateView.as_view(template_name="dashboard/recruiter.html"), name="recruiter"),
    path("admin/", TemplateView.as_view(template_name="dashboard/admin.html"), name="admin"),
]