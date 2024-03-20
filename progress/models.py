from django.db import models


class QuizProgress(models.Model):
    user_id = models.IntegerField(default=0, null=True)
    course = models.IntegerField(default=0, null=True)
    grade = models.FloatField(default=0, null=True)
