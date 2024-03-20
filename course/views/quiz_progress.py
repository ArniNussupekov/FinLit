from rest_framework import viewsets
from rest_framework.response import Response

from course.models import QuizProgress
from course.serializers import QuizProgressSerializer


class QuizProgressViewSet(viewsets.ViewSet):
    def list(self, request):
        quizzes = QuizProgress.objects.all()

        return Response(QuizProgressSerializer(quizzes, many=True).data)

    def create(self, request):
        serializer = QuizProgressSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"success": True, "data": serializer.data})

    def retrieve(self, request, pk):
        try:
            quiz = QuizProgress.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        return Response(QuizProgressSerializer(quiz).data)

    def update(self, request, pk):
        try:
            quiz = QuizProgress.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        serializer = QuizProgressSerializer(instance=quiz, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response({"message": True, "data": serializer.data})

    def delete(self, request, pk):
        try:
            quiz = QuizProgress.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        quiz.delete()
        return Response({"message": True})