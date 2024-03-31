from rest_framework import serializers
from navigator.models import QuizModel, QuizAnswerModel

class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswerModel
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(method_name="get_answers")

    def get_answers(self, quiz):
        answers = QuizAnswerModel.objects.filter(quiz_id=quiz.id)
        serializer = QuizAnswerSerializer(answers, many=True, read_only=True)

        return serializer.data

    class Meta:
        model = QuizModel
        fields = ['id', 'question', 'answers']
