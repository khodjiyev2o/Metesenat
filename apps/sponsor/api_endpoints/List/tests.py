import pytest
from django.urls import reverse
from rest_framework import status

from apps.sponsor.models import SponsorStatus
from tests.factories import SponsorFactory


@pytest.mark.django_db
def test_sponsor_list(client, new_admin_user, new_sponsor):
    url = reverse("sponsor-list")
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(url, **headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["results"][0]["id"] == new_sponsor.id
    assert response.json()["results"][0]["full_name"] == new_sponsor.user.full_name
    assert response.json()["results"][0]["phone"] == new_sponsor.user.phone
    assert response.json()["results"][0]["amount"] == new_sponsor.amount
    assert response.json()["results"][0]["status"] == new_sponsor.status


@pytest.mark.django_db
def test_sponsor_list_search_by_name(client, new_admin_user, new_sponsor):
    url = reverse("sponsor-list")
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(f"{url}?search={new_sponsor.user.full_name}", **headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["results"][0]["id"] == new_sponsor.id
    assert response.json()["results"][0]["full_name"] == new_sponsor.user.full_name
    assert response.json()["results"][0]["phone"] == new_sponsor.user.phone
    assert response.json()["results"][0]["amount"] == new_sponsor.amount
    assert response.json()["results"][0]["status"] == new_sponsor.status


@pytest.mark.django_db
def test_sponsor_list_search_by_name_not_found(client, new_admin_user, new_sponsor):
    url = reverse("sponsor-list")
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(f"{url}?search=someufbdsiufbasgfbiab", **headers)

    assert response.json()["results"] == []
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_sponsor_list_filter(client, new_admin_user):
    url = reverse("sponsor-list")
    new_sponsor = SponsorFactory(status=SponsorStatus.ACCEPTED)
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(f"{url}?status={SponsorStatus.ACCEPTED}", **headers)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["results"][0]["id"] == new_sponsor.id
    assert response.json()["results"][0]["full_name"] == new_sponsor.user.full_name
    assert response.json()["results"][0]["phone"] == new_sponsor.user.phone
    assert response.json()["results"][0]["amount"] == new_sponsor.amount
    assert response.json()["results"][0]["status"] == new_sponsor.status


@pytest.mark.django_db
def test_sponsor_list_filter_not_found(client, new_admin_user):
    url = reverse("sponsor-list")
    SponsorFactory(status=SponsorStatus.ACCEPTED)
    headers = {
        "HTTP_AUTHORIZATION": f"Bearer {new_admin_user.tokens.get('access')}",
    }
    response = client.get(f"{url}?status={SponsorStatus.IN_MODERATION}", **headers)

    assert response.json()["results"] == []
    assert response.status_code == status.HTTP_200_OK
