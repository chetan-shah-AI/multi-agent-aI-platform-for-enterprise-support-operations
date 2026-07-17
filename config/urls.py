from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def health_check(request):
    return JsonResponse(
        {
            "status": "ok",
            "service": "multi-agent-aI-platform-for-enterprise-support-operations",
        }
    )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health_check),
]