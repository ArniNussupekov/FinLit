from django.db import models


class FinancialTrialModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    question = models.CharField(max_length=500)


class FinancialTrialAnswerModel(models.Model):
    fin_id = models.ForeignKey(FinancialTrialModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
