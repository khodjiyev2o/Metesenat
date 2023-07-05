from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from apps.sponsor.api_endpoints import DashboardStatisticsView

from .swagger import swaggerurlpatterns


urlpatterns = [
    path("@dmin/", admin.site.urls),
    path("api/dashboard/", DashboardStatisticsView.as_view(), name="dashboard-statistics"),
    path("api/users/", include("apps.users.urls")),
    path("api/sponsor/", include("apps.sponsor.urls")),
    path("api/social_auth/", include("apps.social_auth.urls")),
]

urlpatterns += swaggerurlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
