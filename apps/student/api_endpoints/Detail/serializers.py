from rest_framework import serializers

from apps.sponsor.models import SponsorShip
from apps.student.models import Student, University


class StudentSponsorSerializer(serializers.ModelSerializer):
    sponsor_name = serializers.CharField(source="sponsor.user.full_name")

    class Meta:
        model = SponsorShip
        fields = ("id", "amount", "sponsor_name")


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ("id", "name")


class StudentDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name")
    university = UniversitySerializer()
    sponsors = StudentSponsorSerializer(many=True)

    class Meta:
        model = Student
        fields = ("id", "full_name", "type", "university", "tuition_fee", "dedicated_amount", "sponsors")
