from django.db import models


class QuizProgress(models.Model):
    user_id = models.IntegerField(default=0, null=True)
    course_id = models.IntegerField(default=0, null=True)
    grade = models.FloatField(default=0, null=True)


class CourseProgress(models.Model):
    user_id = models.IntegerField(default=0)
    course_id = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    percent = models.FloatField(default=0)
    quiz_done = models.BooleanField
    is_completed = models.BooleanField(default=False)

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
    lesson_id = models.IntegerField(default=0)
    course_progress = models.ForeignKey(CourseProgress, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
