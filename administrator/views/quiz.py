from rest_framework.viewsets import ModelViewSet
from course.models import QuizModel

from administrator.serializers import AdminQuizSerializer


class AdminQuizViewSet(ModelViewSet):
    queryset = QuizModel.objects.all()
    serializer_class = AdminQuizSerializer
