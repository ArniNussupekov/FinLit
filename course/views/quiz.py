from rest_framework import viewsets, pagination
from rest_framework.decorators import action
from rest_framework.response import Response

from course.models import QuizModel
from course.serializers import QuizSerializer, QuizAnswerSerializer


class QuizPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100


class QuizViewSet(viewsets.ViewSet):
    pagination_class = QuizPagination

    def list(self, request):
        course_id = request.query_params.get("course_id")
        quizzes = QuizModel.objects.filter(course_id=course_id)

        paginator = self.pagination_class()
        paginated_quizzes = paginator.paginate_queryset(quizzes, request)

        serializer = QuizSerializer(paginated_quizzes, many=True)

        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = QuizSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"success": True, "data": serializer.data})

    @action(detail=False, methods=['post'])
    def add_answers(self, request):
        serializer = QuizAnswerSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"success": True, "data": serializer.data})

    def retrieve(self, request, pk):
        try:
            quiz = QuizModel.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        return Response(QuizSerializer(quiz).data)

    def update(self, request, pk):
        try:
            quiz = QuizModel.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        serializer = QuizSerializer(instance=quiz, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response({"message": True, "data": serializer.data})

    def delete(self, request, pk):
        try:
            quiz = QuizModel.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        quiz.delete()
        return Response({"message": True})
