# Generated by Django 4.2.11 on 2024-03-25 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0)),
                ('votes_sum', models.FloatField(default=0)),
                ('votes', models.IntegerField(default=0)),
                ('module', models.IntegerField(default=1)),
                ('category', models.CharField(default='Money', max_length=255)),
                ('course_num', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QuizModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField(default=0, null=True)),
                ('question', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizAnswerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.quizmodel')),
            ],
        ),
        migrations.CreateModel(
            name='LessonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_num', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='course.coursemodel')),
            ],
        ),
    ]
