from django.db import models


class CourseModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    votes_sum = models.FloatField(default=0)
    votes = models.IntegerField(default=0)
    module = models.IntegerField(default=1)
    category = models.CharField(max_length=255, default="Money")
    course_num = models.IntegerField(default=0)
    is_free = models.BooleanField(default=True, blank=True)
    cost = models.IntegerField(default=0, blank=True)
    img = models.ImageField(upload_to='images/', null=True, blank=True)
  

class LessonModel(models.Model):
    lesson_num = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    url = models.CharField(null=True, max_length=500, default=None)
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True)


class Accordion(models.Model):
    lesson = models.ForeignKey(LessonModel, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    answer = models.TextField()


# some shit logic
class QuizModel(models.Model):
    course_id = models.IntegerField(default=0, null=True)
    question = models.CharField(max_length=255, null=True)


class QuizAnswerModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=True)
