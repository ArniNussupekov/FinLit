# Generated by Django 4.2.13 on 2024-06-11 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_is_verified_emailverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='unicode',
            field=models.IntegerField(default=None, null=True, unique=True),
        ),
    ]
