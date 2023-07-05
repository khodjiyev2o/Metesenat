from django.db.models import Sum
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.sponsor.models import Sponsor
from apps.student.models import Student


class DashboardStatisticsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        donated_amount = Sponsor.objects.aggregate(donated_amount=Sum("amount"))["donated_amount"] or 0
        total_amount = Student.objects.aggregate(total_amount=Sum("tuition_fee"))["total_amount"] or 0
        necessary_amount = total_amount - donated_amount

        return Response(
            {
                "donated_amount": donated_amount,
                "total_amount": total_amount,
                "necessary_amount": necessary_amount,
            },
            status=status.HTTP_200_OK,
        )


__all__ = ["DashboardStatisticsView"]
