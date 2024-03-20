from rest_framework.viewsets import ModelViewSet
from course.models import CourseModel

from administrator.serializers import AdminCourseSerializer


class AdminCourseViewSet(ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = AdminCourseSerializer
