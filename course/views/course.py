from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from course.models import CourseModel
from user.models import User
from progress.models import CourseProgress

from course.serializers import CourseSerializer, CourseRetrieveSerializer


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
        user_id = request.query_params.get("user_id")

        try:
            course = CourseModel.objects.get(id=pk)
        except Exception as e:
            raise "Object not found"
        serializer = CourseRetrieveSerializer(course, context={'user_id': user_id})

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

    @action(detail=False, methods=["get"])
    def get_my_courses(self, request):
        user_id = request.query_params.get("user_id")

        try:
            user = User.objects.get(id=user_id)
        except Exception as e:
            raise e

        progress = CourseProgress.objects.filter(Q(user_id=user_id) & Q(status=CourseProgress.Status.LEARNING))
        course_ids = progress.values_list('course_id', flat=True)
        courses = CourseModel.objects.filter(id__in=course_ids)

        return Response(CourseSerializer(courses, many=True).data)

    @action(detail=False, methods=["get"])
    def get_bookmark(self, request):
        user_id = request.query_params.get("user_id")
        user = User.objects.get(id=user_id)
        serializer = CourseSerializer(user.bookmarked_courses, many=True)

        return Response(serializer.data)


    # Make refactor
    @action(detail=True, methods=['put'])
    def add_bookmark(self, request, pk):
        user_id = request.query_params.get("user_id")

        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=pk)
        except Exception as e:
            raise e

        user.bookmarked_courses.add(course)

        return Response({"Success:": True})

    @action(detail=True, methods=['put'])
    def remove_bookmark(self, request, pk):
        user_id = request.query_params.get("user_id")

        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=pk)
        except Exception as e:
            raise e

        user.bookmarked_courses.remove(course)

        return Response({"Success:": True})
