from django.urls import path

from apps.sponsor.api_endpoints import SponsorRegisterView, SponsorListView, SponsorDetailUpdateView


urlpatterns = [
    path("", SponsorListView.as_view(), name="sponsor-list"),
    path("<int:pk>", SponsorDetailUpdateView.as_view(), name="sponsor-retrieve-update"),
    path("register/", SponsorRegisterView.as_view(), name="sponsor-register"),
]
