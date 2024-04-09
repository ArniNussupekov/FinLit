from django.db import models
from django.contrib.auth.models import AbstractUser

from course.models import CourseModel


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    phone = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    bookmarked_courses = models.ManyToManyField(CourseModel, blank=True)
    balance = models.IntegerField(default=0, blank=True)


class CourseProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False)
    course = models.ForeignKey(CourseModel, on_delete=models.DO_NOTHING, null=False)
    is_completed = models.BooleanField(default=False, blank=True)

    class Meta:
        unique_together = ('user', 'course',)
