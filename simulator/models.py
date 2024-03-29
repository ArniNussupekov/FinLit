from django.db import models


class FinancialTrialModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    level = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    question = models.CharField(max_length=500, null=True)
    situation = models.CharField(max_length=500, null=True)


class FinancialTrialAnswerModel(models.Model):
    fin_id = models.ForeignKey(FinancialTrialModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
