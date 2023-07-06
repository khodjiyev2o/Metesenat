import pytest
from django.urls import reverse
from rest_framework import status

from apps.student.models import StudentType
from tests.fixtures import SponsorShipFactory, StudentFactory


@pytest.mark.django_db
def test_student_list(client, new_admin_user, new_student):
    new_sponsorship = SponsorShipFactory(student=new_student, amount=500)
    url = reverse("student-list")
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(url, **headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["results"][0]["id"] == new_student.id
    assert response.json()["results"][0]["full_name"] == new_student.user.full_name
    assert response.json()["results"][0]["tuition_fee"] == new_student.tuition_fee
    assert response.json()["results"][0]["type"] == new_student.type
    assert response.json()["results"][0]["dedicated_amount"] == new_sponsorship.amount


@pytest.mark.django_db
def test_student_list_search_by_name(client, new_admin_user, new_student):
    url = reverse("student-list")
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(f"{url}?search={new_student.user.full_name}", **headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["results"][0]["id"] == new_student.id
    assert response.json()["results"][0]["full_name"] == new_student.user.full_name
    assert response.json()["results"][0]["tuition_fee"] == new_student.tuition_fee
    assert response.json()["results"][0]["type"] == new_student.type
    assert response.json()["results"][0]["dedicated_amount"] == 0


@pytest.mark.django_db
def test_student_list_search_by_name_not_found(client, new_admin_user, new_student):
    url = reverse("student-list")
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(f"{url}?search=someufbdsiufbasgfbiab", **headers)

    assert response.json()["results"] == []
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_student_list_filter(client, new_admin_user):
    url = reverse("student-list")
    new_student = StudentFactory(type=StudentType.BACHELOR)
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(f"{url}?type={StudentType.BACHELOR}", **headers)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["results"][0]["id"] == new_student.id
    assert response.json()["results"][0]["full_name"] == new_student.user.full_name
    assert response.json()["results"][0]["tuition_fee"] == new_student.tuition_fee
    assert response.json()["results"][0]["type"] == new_student.type
    assert response.json()["results"][0]["dedicated_amount"] == 0


@pytest.mark.django_db
def test_student_list_filter_not_found(client, new_admin_user):
    url = reverse("student-list")
    StudentFactory(type=StudentType.MASTERS)
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(f"{url}?type={StudentType.BACHELOR}", **headers)

    assert response.json()["results"] == []
    assert response.status_code == status.HTTP_200_OK
