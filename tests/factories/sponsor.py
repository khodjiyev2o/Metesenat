import factory

from apps.sponsor.models import Payment, Sponsor, SponsorStatus, SponsorType


class SponsorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sponsor

    user = factory.SubFactory("tests.factories.user.UserFactory")
    type = factory.Iterator(SponsorType.choices)
    status = SponsorStatus.IN_MODERATION
    company = factory.Faker("company")
    amount = factory.Faker("pyint", min_value=1000)
    payment_type = factory.Iterator(Payment.choices)
    comment = factory.Faker("text")


__all__ = ["SponsorFactory"]
