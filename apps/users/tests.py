import pytest
from django.urls import reverse
from rest_framework import status
from apps.users.models import User

@pytest.mark.django_db
def test_user_manager(client):
    User.objects.create_user(email="samandarkhodjiyev@gmail.com")

    assert User.objects.count() == 1

@pytest.mark.django_db
def test_user_manager_without_email_phone():
    with pytest.raises(ValueError) as exception_info:
        User.objects.create_user(full_name="samandarkhodjiyev@gmail.com")

    assert str(exception_info.value) == "User must have either an email or phone!"


@pytest.mark.django_db
def test_superuser_manager(client):
    User.objects.create_superuser(email="samandarkhodjiyev@gmail.com", password="some_passowrd1234")
    assert User.objects.filter(is_superuser=True).count() == 1

@pytest.mark.django_db
def test_create_superuser():
    with pytest.raises(ValueError) as exception_info:
        User.objects.create_superuser(email="samandarkhodjiyev@gmail.com", password=None)

    assert str(exception_info.value) == "User must have  password!"


@pytest.mark.django_db
def test_user_tokens(client):
    new_user = User.objects.create_superuser(email="samandarkhodjiyev@gmail.com", password="some_passowrd1234")
    assert User.objects.filter(is_superuser=True).count() == 1
    assert list(new_user.tokens.keys()) == ['access', 'refresh']



@pytest.mark.django_db
def test_user_model_str_method(client):
    new_user = User.objects.create_superuser(email="samandarkhodjiyev@gmail.com", password="some_passowrd1234")
    assert User.__str__(new_user) == new_user.email

    new_user = User.objects.create(phone="+998913665113")
    assert User.__str__(new_user) == new_user.phone
