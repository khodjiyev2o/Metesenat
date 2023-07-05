import pytest
from pytest_factoryboy import register

from tests.factories import SponsorFactory


register(SponsorFactory)


@pytest.fixture()
def new_sponsor(db, sponsor_factory):
    return sponsor_factory.create()
