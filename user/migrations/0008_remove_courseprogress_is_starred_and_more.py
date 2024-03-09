# Generated by Django 4.2.10 on 2024-03-09 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_remove_coursemodel_lesson_lessonmodel_course'),
        ('user', '0007_remove_user_starred_courses_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseprogress',
            name='is_starred',
        ),
        migrations.AddField(
            model_name='user',
            name='bookmarked_courses',
            field=models.ManyToManyField(null=True, to='course.coursemodel'),
        ),
    ]
