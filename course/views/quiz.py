from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from course.models import QuizModel
from course.serializers import QuizSerializer


class QuizViewSet(viewsets.ViewSet):
    def list(self, request):
        course_id = request.query_params.get("course_id")
        quizzes = QuizModel.objects.filter(course_id=course_id)

        return Response(QuizSerializer(quizzes, many=True).data)

    def create(self, request):
        serializer = QuizSerializer(data=request.data)
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
