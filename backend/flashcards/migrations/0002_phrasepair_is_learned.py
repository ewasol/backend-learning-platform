# Generated by Django 5.0.6 on 2024-07-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flashcards", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="phrasepair",
            name="is_learned",
            field=models.BooleanField(default=False),
        ),
    ]