# Generated by Django 4.2 on 2023-07-06 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0002_remove_student_sponsors"),
        ("sponsor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SponsorShip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(default=1000, verbose_name="Amount of Money"),
                ),
                (
                    "sponsor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sponsor.sponsor",
                        verbose_name="Sponsor",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="student.student",
                        verbose_name="Student",
                    ),
                ),
            ],
            options={
                "verbose_name": "Sponsorship",
                "verbose_name_plural": "Sponsorships",
            },
        ),
    ]
