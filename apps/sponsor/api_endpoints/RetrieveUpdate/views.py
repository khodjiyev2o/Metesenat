from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser

from apps.sponsor.api_endpoints.RetrieveUpdate.serializers import (
    SponsorDetailUpdateSerializer,
)
from apps.sponsor.models import Sponsor


class SponsorDetailUpdateView(RetrieveUpdateAPIView):
    serializer_class = SponsorDetailUpdateSerializer
    queryset = Sponsor.objects.all()
    permission_classes = [IsAdminUser]


__all__ = ["SponsorDetailUpdateView"]
