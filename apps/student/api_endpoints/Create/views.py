from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser

from apps.student.api_endpoints.Create.serializers import StudentAddSerializer
from apps.student.models import Student


class StudentAddView(CreateAPIView):
    """Authentication is required"""

    queryset = Student.objects.all()
    serializer_class = StudentAddSerializer
    permission_classes = [IsAdminUser]


__all__ = ["StudentAddView"]
