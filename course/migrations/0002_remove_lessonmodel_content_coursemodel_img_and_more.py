# Generated by Django 4.2.13 on 2024-05-09 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessonmodel',
            name='content',
        ),
        migrations.AddField(
            model_name='coursemodel',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='lessonmodel',
            name='url',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
