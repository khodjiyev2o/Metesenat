from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from apps.sponsor.models import SponsorShip
from apps.student.api_endpoints.SponsorshipUpdate.serializers import (
    StudentSponsorSerializer,
)


class StudentSponsorshipUpdateView(UpdateAPIView):
    queryset = SponsorShip.objects.all()
    serializer_class = StudentSponsorSerializer
    permission_classes = [IsAdminUser]


__all__ = ["StudentSponsorshipUpdateView"]
