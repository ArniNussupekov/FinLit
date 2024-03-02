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

    def update(self, request, pk):
        try:
            lesson = LessonModel.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        serializer = LessonSerializer(instance=lesson, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response({"message": True, "data": serializer.data})


