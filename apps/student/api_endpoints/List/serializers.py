from rest_framework import serializers

from apps.student.models import Student


class StudentListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name")
    university = serializers.CharField(source="university.name")

    class Meta:
        model = Student
        fields = ("id", "full_name", "type", "university", "tuition_fee", "dedicated_amount")
