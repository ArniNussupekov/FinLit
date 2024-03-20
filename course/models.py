from django.db import models


class CourseModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    module = models.IntegerField(default=1)
    category = models.CharField(max_length=255, default="Money")
    course_num = models.IntegerField(default=0)
  

class LessonModel(models.Model):
    lesson_num = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE, null=True)


# some shit logic
class QuizModel(models.Model):
    course_id = models.IntegerField(default=0, null=True)
    question = models.CharField(max_length=255, null=True)


class QuizAnswerModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=True)
