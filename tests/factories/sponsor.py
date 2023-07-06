import factory

from apps.sponsor.models import (
    Payment,
    Sponsor,
    SponsorShip,
    SponsorStatus,
    SponsorType,
)


class SponsorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Sponsor

    user = factory.SubFactory("tests.factories.user.UserFactory")
    type = SponsorType.INDIVIDUAL
    status = SponsorStatus.IN_MODERATION
    company = factory.Faker("company")
    amount = factory.Faker("pyint", min_value=1000)
    payment_type = Payment.CASH
    comment = factory.Faker("text")


class SponsorShipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SponsorShip

    sponsor = factory.SubFactory("tests.factories.sponsor.SponsorFactory")
    student = factory.SubFactory("tests.factories.student.StudentFactory")


__all__ = ["SponsorFactory", "SponsorShipFactory"]
