import pytest

from apps.sponsor.models import Sponsor


@pytest.mark.django_db
def test_sponsor_model_str_method(client, new_sponsor):

    assert Sponsor.__str__(new_sponsor) == new_sponsor.user.full_name
