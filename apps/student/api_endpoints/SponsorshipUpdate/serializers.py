from rest_framework import serializers

from apps.sponsor.models import SponsorShip


class StudentSponsorSerializer(serializers.ModelSerializer):
    sponsor_name = serializers.CharField(source="sponsor.user.full_name", read_only=True)

    class Meta:
        model = SponsorShip
        fields = ("id", "amount", "sponsor_name")
