from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from apps.student.api_endpoints.List.serializers import StudentListSerializer
from apps.student.models import Student


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [IsAdminUser]
    search_fields = ("user__full_name",)
    filterset_fields = ("type",)


__all__ = ["StudentListView"]
