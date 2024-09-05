# Generated by Django 5.0.6 on 2024-09-04 17:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flashcards", "0002_phrasepair_is_learned"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="user",
            field=models.ForeignKey(
                default="1",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]