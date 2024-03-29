from rest_framework import serializers
from .models import FinancialTrialModel


class FinancialTrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialTrialModel
        fields = '__all__'
