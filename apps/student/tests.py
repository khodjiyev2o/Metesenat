import pytest

from apps.student.models import Student, University


@pytest.mark.django_db
def test_student_model_str_method(client, new_student):

    assert Student.__str__(new_student) == new_student.user.full_name


@pytest.mark.django_db
def test_university_model_str_method(client, new_university):

    assert University.__str__(new_university) == new_university.name
