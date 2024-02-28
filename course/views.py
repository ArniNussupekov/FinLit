from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from .models import CourseModel
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ViewSet):

    def list(self, request):
        courses = CourseModel.objects.filter(Q(category=request.data["Bank"]) |
                                             Q(category=request.data["Investment"]) |
                                             Q(category=request.data["Credit"]) |
                                             Q(category=request.data["Currency"]) |
                                             Q(category=request.data["Stock"]) |
                                             Q(category=request.data["Money"]))
        serializer = CourseSerializer(courses, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"success": True, "data": serializer.data})

    def retrieve(self, request, pk):
        course = CourseModel.objects.get(id=pk)
        serializer = CourseSerializer(course)

        return Response(serializer.data)

    def update(self, request, pk):
        course = CourseModel.objects.get(id=pk)
        serializer = CourseSerializer(instance=course, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response({"Success": True, "data": serializer.data})

    def delete(self, request, pk):
        course = CourseModel.objects.get(id=pk)
        course.delete()

        return Response({"Success": True})
