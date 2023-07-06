from rest_framework import serializers

from apps.student.models import Student
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone", "full_name")


class StudentAddSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = (
            "user",
            "university",
            "type",
            "tuition_fee",
        )

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user = User.objects.create(**user_data)

        return Student.objects.create(user=user, **validated_data)
