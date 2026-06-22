from django.urls import path
from .views import JobCandidatesAPIView, RecruiterJobDetailAPIView, RecruiterJobsAPIView

app_name = 'recruiters'

urlpatterns = [
    path("jobs/", RecruiterJobsAPIView.as_view(), name="jobs"),
    path("jobs/<int:pk>/", RecruiterJobDetailAPIView.as_view(), name="job-detail"),
    path("jobs/<int:pk>/candidates/", JobCandidatesAPIView.as_view(), name="job-candidates"),
]