import factory

from apps.student.models import University


class UniversityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = University

    name = factory.Faker("word")


__all__ = ["UniversityFactory"]
