from django.db import models


class QuizModel(models.Model):
    question = models.CharField(max_length=255, null=True)


class QuizAnswerModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    