# Generated by Django 4.2.4 on 2023-08-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0002_post_tag_alter_slider_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="slider",
            name="image",
            field=models.ImageField(upload_to="images/sliders/"),
        ),
    ]