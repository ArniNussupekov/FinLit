from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from course.models import LessonModel
from course.serializers import LessonSerializer


class LessonViewSet(viewsets.ViewSet):
    def list(self, request):
        lesson = LessonModel.objects.all()

        return Response(LessonSerializer(lesson, many=True).data)

    def create(self, request):
        serializer = LessonSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"success": True, "data": serializer.data})

    def retrieve(self, request, pk):
        try:
            lesson = LessonModel.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        return Response(LessonSerializer(lesson).data)

    def update(self, request, pk):
        try:
            lesson = LessonModel.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        serializer = LessonSerializer(instance=lesson, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response({"message": True, "data": serializer.data})

    @action(detail=True, methods=["get"])
    def get_lessons(self, request, pk):
        lessons = LessonModel.objects.filter(course_id=pk)

        return Response(LessonSerializer(lessons, many=True).data)
