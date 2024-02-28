from django.db import models


class LessonModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()


class CourseModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    module = models.IntegerField(default=1)
    category = models.CharField(max_length=255, default="Money")
    lesson = models.ForeignKey(LessonModel, on_delete=models.CASCADE, null=True)
