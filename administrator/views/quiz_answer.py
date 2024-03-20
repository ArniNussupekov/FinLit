from rest_framework.viewsets import ModelViewSet
from course.models import QuizAnswerModel

from administrator.serializers import AdminQuizAnswerSerializer


class AdminQuizAnswerViewSet(ModelViewSet):
    queryset = QuizAnswerModel.objects.all()
    serializer_class = AdminQuizAnswerSerializer
