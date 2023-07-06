from rest_framework import serializers

from apps.sponsor.models import Sponsor


class SponsorListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name")
    phone = serializers.CharField(source="user.phone")

    class Meta:
        model = Sponsor
        fields = ("id", "full_name", "phone", "amount", "created_at", "status")
