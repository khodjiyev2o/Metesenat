from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.student.models import Student
from apps.users.models import User


class SponsorType(models.TextChoices):
    LEGAL = "legal", _("Legal")
    INDIVIDUAL = "individual", _("Individual")


class SponsorStatus(models.TextChoices):
    NEW = "new", _("New")
    IN_MODERATION = "in_moderation", _("In Moderation")
    DECLINED = "declined", _("Declined")
    ACCEPTED = "accepted", _("Accepted")


class Payment(models.TextChoices):
    CASH = "cash", _("Cash")
    CARD = "card", _("Card")
    TRANSFER = "transfer", _("Transfer")


class Sponsor(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    type = models.CharField(max_length=256, default=SponsorType.INDIVIDUAL, choices=SponsorType.choices)
    status = models.CharField(max_length=256, default=SponsorStatus.IN_MODERATION, choices=SponsorStatus.choices)
    company = models.CharField(max_length=256, verbose_name=_("Company Name"), null=True, blank=True)
    amount = models.PositiveIntegerField(default=1000, verbose_name=_("Amount of Money"))
    payment_type = models.CharField(max_length=256, default=Payment.CASH, choices=Payment.choices)
    comment = models.TextField(verbose_name=_("Comment"))

    def __str__(self):
        return self.user.full_name

    @property
    def left_money(self):
        sponsored_amount = self.sponsorships.aggregate(amount=models.Sum("amount"))["amount"] or 0
        return self.amount - sponsored_amount

    class Meta:
        verbose_name = _("Sponsor")
        verbose_name_plural = _("Sponsors")


class SponsorShip(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name=_("Student"), related_name="sponsors")
    sponsor = models.ForeignKey(
        Sponsor, on_delete=models.CASCADE, verbose_name=_("Sponsor"), related_name="sponsorships"
    )
    amount = models.PositiveIntegerField(default=1000, verbose_name=_("Amount of Money"))

    def __str__(self):
        return f"{self.sponsor.user.full_name} sponsored to {self.student.user.full_name}"

    def clean(self):
        """Check if there is enough money of sponsor to donate"""
        if self.sponsor.left_money < self.amount:
            raise ValidationError(_("Sorry, sponsor does not have enough money"))

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Sponsorship")
        verbose_name_plural = _("Sponsorships")
