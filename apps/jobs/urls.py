from django.urls import path
from django.views.generic import TemplateView
from .views import (
    ApplyJobAPIView, AIMatchAPIView, FilterJobsAPIView,
    MarkRecentlyViewedJobAPIView, RecentlyViewedJobsAPIView,
    RecommendedJobsAPIView, SavedJobsAPIView, ToggleSavedJobAPIView,
)

app_name = 'jobs'

urlpatterns = [
    # FRONTEND
    path("", TemplateView.as_view(template_name="jobs.html"), name="list"),
    
    # API
    path("recommended/", RecommendedJobsAPIView.as_view(), name="api-recommended"),
    path("ai-match/", AIMatchAPIView.as_view(), name="api-ai-match"),
    path("apply/<int:pk>/", ApplyJobAPIView.as_view(), name="api-apply"),
    path("filter/", FilterJobsAPIView.as_view(), name="api-filter"),
    path("saved/", SavedJobsAPIView.as_view(), name="api-saved"),
    path("saved/<int:pk>/", ToggleSavedJobAPIView.as_view(), name="api-save-toggle"),
    path("recent/", RecentlyViewedJobsAPIView.as_view(), name="api-recent"),
    path("viewed/<int:pk>/", MarkRecentlyViewedJobAPIView.as_view(), name="api-viewed"),
]