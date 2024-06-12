from django.db import models
from django.contrib.postgres.fields import ArrayField


class QuizProgress(models.Model):
    user_id = models.IntegerField(default=0, null=True)
    course_id = models.IntegerField(default=0, null=True)
    grade = models.FloatField(default=0, null=True)
    user_choices = ArrayField(models.IntegerField(), null=True)


class CourseProgress(models.Model):
    user_id = models.IntegerField(default=0)
    course_id = models.IntegerField(default=0)
    course_level = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    percent = models.FloatField(default=0)
    quiz_done = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    feedback_sent = models.BooleanField(default=False)

    class Status(models.TextChoices):
        LEARNING = "LEARNING", "Learning"
        COMPLETED = "COMPLETED", "Completed"

    status = models.CharField(
        max_length=255,
        choices=Status.choices,
        default=None,
        null=True,
        blank=True
    )


class LessonProgress(models.Model):
    user_id = models.IntegerField(default=0)
    course_id = models.IntegerField(default=0)
    lesson_id = models.IntegerField(default=0)
    course_progress = models.ForeignKey(CourseProgress, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
