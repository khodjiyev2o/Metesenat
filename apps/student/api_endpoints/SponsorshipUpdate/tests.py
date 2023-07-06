import pytest
from django.urls import reverse

from apps.student.models import StudentType


@pytest.mark.django_db
def test_sponsorship_update(client, new_admin_user, new_sponsorship):
    url = reverse("student-sponsorship-update", kwargs={"pk": new_sponsorship.id})
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    data = {
        "amount": 100,
    }
    response = client.patch(url, data=data, content_type="application/json", **headers)
    assert response.status_code == 200
    assert response.json()['id'] == new_sponsorship.id
    assert response.json()['sponsor_name'] == new_sponsorship.sponsor.user.full_name
    assert response.json()['amount'] == data['amount']


@pytest.mark.django_db
def test_sponsorship_update_no_admin(client, new_user, new_sponsorship):
    url = reverse("student-sponsorship-update", kwargs={"pk": new_sponsorship.id})
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_user.tokens.get('access')}",
    }
    data = {
        "amount": 500,
    }
    response = client.patch(url, data=data, content_type="application/json", **headers)

    assert response.status_code == 403
    assert response.json()["detail"] == "You do not have permission to perform this action."
