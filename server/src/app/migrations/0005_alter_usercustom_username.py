# Generated by Django 5.1 on 2024-08-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_usercustom_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usercustom",
            name="username",
            field=models.CharField(max_length=200),
        ),
    ]
