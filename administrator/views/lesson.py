from rest_framework.viewsets import ModelViewSet
from course.models import LessonModel

from administrator.serializers import AdminLessonSerializer


class AdminLessonViewSet(ModelViewSet):
    queryset = LessonModel.objects.all()
    serializer_class = AdminLessonSerializer
