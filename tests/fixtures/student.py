import pytest
from pytest_factoryboy import register

from tests.factories import StudentFactory


register(StudentFactory)


@pytest.fixture()
def new_student(db, student_factory):
    return student_factory.create()
