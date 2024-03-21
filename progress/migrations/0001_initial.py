# Generated by Django 4.2.11 on 2024-03-21 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('course_id', models.IntegerField(default=0)),
                ('percent', models.FloatField(default=0)),
                ('status', models.CharField(blank=True, choices=[('LEARNING', 'Learning'), ('COMPLETED', 'Completed')], default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0, null=True)),
                ('course_id', models.IntegerField(default=0, null=True)),
                ('grade', models.FloatField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LessonProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('lesson_id', models.IntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('course_progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='progress.courseprogress')),
            ],
        ),
    ]
