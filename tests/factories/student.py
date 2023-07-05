import factory

from apps.student.models import Student, StudentType


class StudentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Student

    user = factory.SubFactory("tests.factories.user.UserFactory")
    type = factory.Iterator(StudentType.choices)
    university = factory.SubFactory("tests.factories.university.UniversityFactory")
    tuition_fee = factory.Faker("pyint")


__all__ = ["StudentFactory"]
