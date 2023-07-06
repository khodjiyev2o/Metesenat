import pytest
from django.urls import reverse

from apps.student.models import StudentType


@pytest.mark.django_db
def test_student_update(client, new_admin_user, new_student, new_university):
    url = reverse("student-update", kwargs={"pk": new_student.id})
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    data = {
        "user": {"full_name": "New_updated_name", "phone": "+998913582680"},
        "type": StudentType.BACHELOR,
        "tuition_fee": 100000,
        "university": new_university.id,
    }
    response = client.patch(url, data=data, content_type="application/json", **headers)

    assert response.json()["id"] == new_student.id
    assert response.json()["type"] == data["type"]
    assert response.json()["tuition_fee"] == data["tuition_fee"]
    assert response.json()["university"] == data["university"]
    assert response.json()["user"]["full_name"] == data["user"]["full_name"]


@pytest.mark.django_db
def test_student_update_no_admin(client, new_user, new_student, new_university):
    url = reverse("student-update", kwargs={"pk": new_student.id})
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_user.tokens.get('access')}",
    }
    data = {
        "user": {"full_name": "New_updated_name", "phone": "+998913582680"},
        "type": StudentType.BACHELOR,
        "tuition_fee": 100000,
        "university": new_university.id,
    }
    response = client.patch(url, data=data, content_type="application/json", **headers)

    assert response.status_code == 403
    assert response.json()["detail"] == "You do not have permission to perform this action."
