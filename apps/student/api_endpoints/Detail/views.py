from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from apps.student.api_endpoints.Detail.serializers import StudentDetailSerializer
from apps.student.models import Student


class StudentDetailView(RetrieveAPIView):
    serializer_class = StudentDetailSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAdminUser]


__all__ = ["StudentDetailView"]
