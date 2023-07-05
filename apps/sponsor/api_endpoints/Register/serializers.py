from rest_framework import serializers

from apps.sponsor.models import Sponsor
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone", "full_name")


class SponsorRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Sponsor
        fields = ("user", "type", "company", "amount", "payment_type", "comment")

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)

        return Sponsor.objects.create(user=user, **validated_data)
