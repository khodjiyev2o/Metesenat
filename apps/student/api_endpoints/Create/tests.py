import pytest
from django.urls import reverse
from rest_framework import status

from apps.student.models import Student, StudentType


@pytest.mark.django_db
def test_student_add_no_admin(client, new_university):
    url = reverse("student-add")
    payload = {
        "user": {"phone": "+998913665113", "full_name": "Samandar Hojiev"},
        "type": StudentType.BACHELOR,
        "tuition_fee": 100000,
        "university": new_university.id,
    }
    response = client.post(url, data=payload, content_type="application/json")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_student_add(client, new_university, new_admin_user):
    url = reverse("student-add")
    payload = {
        "user": {"phone": "+998913665113", "full_name": "Samandar Hojiev"},
        "type": StudentType.BACHELOR,
        "tuition_fee": 100000,
        "university": new_university.id,
    }
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.post(url, data=payload, content_type="application/json", **headers)
    assert Student.objects.count() == 1
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["user"]["phone"] == payload["user"]["phone"]
    assert response.json()["user"]["full_name"] == payload["user"]["full_name"]
    assert response.json()["university"] == payload["university"]
    assert response.json()["type"] == payload["type"]
    assert response.json()["tuition_fee"] == payload["tuition_fee"]
