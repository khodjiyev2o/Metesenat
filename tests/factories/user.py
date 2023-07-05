import factory

from apps.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    full_name = factory.Faker("word")
    email = factory.Faker("email")
    phone = factory.Faker("phone_number")


__all__ = ["UserFactory"]
