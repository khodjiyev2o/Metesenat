import pytest
from django.urls import reverse

from apps.sponsor.models import Payment, SponsorType


@pytest.mark.django_db
def test_sponsor_update(client, new_admin_user, new_sponsor):
    url = reverse("sponsor-retrieve-update", kwargs={"pk": new_sponsor.id})
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    data = {
        "user": {"full_name": "New_updated_name", "phone": "+998913582680"},
        "type": SponsorType.LEGAL,
        "company": "UIC GROUP",
        "amount": 100000,
        "payment_type": Payment.CARD,
        "comment": "test_Comment",
    }
    response = client.patch(url, data=data, content_type="application/json", **headers)
    assert response.json()["id"] == new_sponsor.id
    assert response.json()["type"] == data["type"]
    assert response.json()["company"] == data["company"]
    assert response.json()["amount"] == data["amount"]
    assert response.json()["payment_type"] == data["payment_type"]


@pytest.mark.django_db
def test_sponsor_detail(client, new_admin_user, new_sponsor):
    url = reverse("sponsor-retrieve-update", kwargs={"pk": new_sponsor.id})
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(url, content_type="application/json", **headers)

    assert response.json()["id"] == new_sponsor.id
    assert response.json()["type"] == new_sponsor.type
    assert response.json()["company"] == new_sponsor.company
    assert response.json()["amount"] == new_sponsor.amount
    assert response.json()["payment_type"] == new_sponsor.payment_type


@pytest.mark.django_db
def test_sponsor_detail_no_admin(client, new_user, new_sponsor):
    url = reverse("sponsor-retrieve-update", kwargs={"pk": new_sponsor.id})
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_user.tokens.get('access')}",
    }
    response = client.get(url, content_type="application/json", **headers)
    assert response.status_code == 403
