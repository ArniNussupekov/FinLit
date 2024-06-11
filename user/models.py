from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail

from course.models import CourseModel


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    username = None
    is_verified = models.BooleanField(default=False)
    unicode = models.IntegerField(null=True, default=None, unique=True)

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


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'Email verification object for {self.user.email}'

    def send_verification_email(self, request):
        title = request["title"]
        message = request["message"]

        send_mail(
            title,
            message,
            'finlit.academy@yandex.ru',
            [self.user.email],
            fail_silently=False,
        )
