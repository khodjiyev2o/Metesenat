# Generated by Django 4.2 on 2023-07-06 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("student", "0002_remove_student_sponsors"),
    ]

    operations = [
        migrations.AlterField(
            model_name="university",
            name="name",
            field=models.CharField(max_length=256, unique=True, verbose_name="Name"),
        ),
    ]
