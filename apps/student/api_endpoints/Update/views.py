from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAdminUser

from apps.student.api_endpoints.Update.serializers import StudentUpdateSerializer
from apps.student.models import Student


class StudentUpdateView(UpdateAPIView):
    serializer_class = StudentUpdateSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAdminUser]


__all__ = ["StudentUpdateView"]
