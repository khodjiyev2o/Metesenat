import pytest
from django.urls import reverse
from rest_framework import status

from apps.sponsor.models import Payment, Sponsor, SponsorType


@pytest.mark.django_db
def test_sponsor_register(client):
    url = reverse("sponsor-register")
    payload = {
        "user": {"phone": "+998913665113", "full_name": "Samandar Hojiev"},
        "type": SponsorType.LEGAL,
        "company": "UIC GROUP",
        "amount": 100000,
        "payment_type": Payment.CASH,
        "comment": "test_Comment",
    }
    response = client.post(url, data=payload, content_type="application/json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Sponsor.objects.count() == 1
