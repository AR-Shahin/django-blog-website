# Generated by Django 4.2.4 on 2023-08-22 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0004_contact"),
    ]

    operations = [
        migrations.RenameField(
            model_name="contact",
            old_name="description",
            new_name="message",
        ),
    ]
