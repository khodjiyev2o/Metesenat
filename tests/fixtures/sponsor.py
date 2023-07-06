import pytest
from pytest_factoryboy import register

from tests.factories import SponsorFactory, SponsorShipFactory


register(SponsorFactory)
register(SponsorShipFactory)


@pytest.fixture()
def new_sponsor(db, sponsor_factory):
    return sponsor_factory.create()


@pytest.fixture()
def new_sponsorship(db, sponsor_ship_factory):
    return sponsor_ship_factory.create()
