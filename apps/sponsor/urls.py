from django.urls import path

from apps.sponsor.api_endpoints import SponsorRegisterView


urlpatterns = [
    path("register/", SponsorRegisterView.as_view(), name="sponsor-register"),
]
