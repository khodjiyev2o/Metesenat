import pytest
from django.core.exceptions import ValidationError
from django.urls import reverse

from tests.factories import SponsorShipFactory


@pytest.mark.django_db
def test_student_detail(client, new_admin_user, new_student):
    new_sponsorship = SponsorShipFactory(student=new_student)
    new_sponsorship_2 = SponsorShipFactory(student=new_student)
    url = reverse("student-detail", kwargs={"pk": new_student.id})
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(url, content_type="application/json", **headers)

    assert response.status_code == 200
    assert response.json()["id"] == new_student.id
    assert response.json()["type"] == new_student.type
    assert response.json()["tuition_fee"] == new_student.tuition_fee
    assert response.json()["university"]["name"] == new_student.university.name
    assert response.json()["dedicated_amount"] == new_sponsorship.amount + new_sponsorship_2.amount
    assert len(response.json()["sponsors"]) == 2


@pytest.mark.django_db
def test_sponsor_not_enough_money(new_student):
    with pytest.raises(ValidationError) as exception_info:
        SponsorShipFactory(student=new_student, amount=10000000)

    assert str(exception_info.value) == "{'__all__': ['Sorry, sponsor does not have enough money']}"
