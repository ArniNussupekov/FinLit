from django.db import models


class NavigatorQuizModel(models.Model):
    question = models.CharField(max_length=255, null=True)


class NavigatorQuizAnswerModel(models.Model):
    quiz = models.ForeignKey(NavigatorQuizModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    