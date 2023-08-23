# Generated by Django 4.2.4 on 2023-08-22 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0005_rename_description_contact_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/category/"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/posts/"),
        ),
    ]