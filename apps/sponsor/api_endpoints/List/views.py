from rest_framework.generics import ListAPIView
from apps.sponsor.models import Sponsor
from apps.sponsor.api_endpoints.List.serializers import SponsorListSerializer
from rest_framework.permissions import IsAdminUser


class SponsorListView(ListAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorListSerializer
    permission_classes = [IsAdminUser]
    search_fields = ("user__full_name",)
    filterset_fields = ("status", "created_at", "amount")


__all__ = ['SponsorListView']
