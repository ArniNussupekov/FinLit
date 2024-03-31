from rest_framework import serializers
from .models import FinancialTrialModel, FinancialTrialAnswerModel


class FinancialTrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialTrialModel
        fields = '__all__'


class TrialAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialTrialAnswerModel
        fields = '__all__'


class FinancialTrialRetrieveSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(method_name="get_answers")

    def get_answers(self, trial):
        answers = FinancialTrialAnswerModel.objects.filter(fin_id=trial.id)
        serializer = TrialAnswerSerializer(answers, many=True, read_only=True)

        return serializer.data

    class Meta:
        model = FinancialTrialModel
        fields = ['name', 'description', 'level', 'category', 'question', 'situation', 'answers']
