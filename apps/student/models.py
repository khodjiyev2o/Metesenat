from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.users.models import User


class StudentType(models.TextChoices):
    BACHELOR = "bachelor", _("Bachelor's")
    MASTERS = "master", _("Master's")


class University(BaseModel):
    name = models.CharField(max_length=256, verbose_name=_("Name"), unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("University")
        verbose_name_plural = _("Universities")


class Student(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    type = models.CharField(max_length=256, default=StudentType.BACHELOR, choices=StudentType.choices)
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name=_("University"))
    tuition_fee = models.PositiveIntegerField(default=1000, verbose_name=_("Amount of Money"))

    def __str__(self):
        return self.user.full_name

    @property
    def dedicated_amount(self):
        return self.sponsors.aggregate(amount=models.Sum("amount"))["amount"] or 0

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")
