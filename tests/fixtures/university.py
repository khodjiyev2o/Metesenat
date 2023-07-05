import pytest
from pytest_factoryboy import register

from tests.factories import UniversityFactory


register(UniversityFactory)


@pytest.fixture()
def new_university(db, university_factory):
    return university_factory.create()
