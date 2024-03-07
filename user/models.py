from django.db import models
from course.models import CourseModel


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField(blank=True, null=True)
    starred_courses = models.ManyToManyField(CourseModel, blank=True)


class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    course = models.ForeignKey(CourseModel, on_delete=models.DO_NOTHING, null=False)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'course',)
