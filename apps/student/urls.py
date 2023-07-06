from django.urls import path

from apps.student.api_endpoints import (
    StudentAddView,
    StudentDetailView,
    StudentListView,
    StudentSponsorshipUpdateView,
    StudentUpdateView,
)


urlpatterns = [
    path("", StudentListView.as_view(), name="student-list"),
    path("add/", StudentAddView.as_view(), name="student-add"),
    path("<int:pk>/", StudentDetailView.as_view(), name="student-detail"),
    path("<int:pk>/update/", StudentUpdateView.as_view(), name="student-update"),
    path("sponsorship/<int:pk>/", StudentSponsorshipUpdateView.as_view(), name="student-sponsorship-update"),
]
