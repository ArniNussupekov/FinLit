from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from .models import CourseModel
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ViewSet):

    def list(self, request):
        module = request.query_params.get("Module")
        filters = {
            "bank": request.query_params.get("Bank", None),
            "investment": request.query_params.get("Investment", None),
            "credit": request.query_params.get("Credit", None),
            "currency": request.query_params.get("Currency", None),
            "stock": request.query_params.get("Stock", None),
            "money": request.query_params.get("Money", None),
        }

        query = Q()
        for key, value in filters.items():
            if value:
                query |= Q(category=value)

        courses = CourseModel.objects.filter(query)
        courses = courses.filter(module=module)
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
