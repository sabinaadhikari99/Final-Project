from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("django-admin/", admin.site.urls),
    
    # ==================== FRONTEND ROUTES ====================
    path("", include("apps.accounts.urls")),
    path("dashboard/", include("apps.dashboard.urls")),
    path("jobs/", include("apps.jobs.urls")),
    path("skillgap/", include("apps.skillgap.urls")),
    path("recommendations/", include("apps.recommendations.urls")),
    path("notifications/", include("apps.notifications.urls")),
    path("chat/", include("apps.chatbot.urls")),
    path("quiz/", include("apps.quiz.urls")),
    path("external/", include("apps.external.urls")),
    
    # ==================== API ROUTES ====================
    path("api/auth/", include(("apps.accounts.urls", "accounts"), namespace="api-accounts")),
    path("api/jobs/", include(("apps.jobs.urls", "jobs"), namespace="api-jobs")),
    path("api/skillgap/", include(("apps.skillgap.urls", "skillgap"), namespace="api-skillgap")),
    path("api/recruiter/", include(("apps.recruiters.urls", "recruiters"), namespace="api-recruiters")),
    path("api/admin/", include(("apps.admin_panel.urls", "admin_panel"), namespace="api-admin")),
    path("api/chatbot/", include(("apps.chatbot.urls", "chatbot"), namespace="api-chatbot")),
    path("api/quiz/", include(("apps.quiz.urls", "quiz"), namespace="api-quiz")),
    path("api/external/", include(("apps.external.urls", "external"), namespace="api-external")),
    path("api/notifications/", include(("apps.notifications.urls", "notifications"), namespace="api-notifications")),
]

admin.site.site_header = "SkillSync AI Admin"