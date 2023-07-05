from rest_framework.generics import CreateAPIView

from apps.sponsor.api_endpoints.Register.serializers import SponsorRegisterSerializer
from apps.sponsor.models import Sponsor


class SponsorRegisterView(CreateAPIView):
    """Authentication is not required"""

    queryset = Sponsor.objects.all()
    serializer_class = SponsorRegisterSerializer


__all__ = ['SponsorRegisterView']
