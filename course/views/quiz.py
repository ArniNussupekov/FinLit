from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from course.models import QuizModel, CourseModel, QuizProgress
from user.models import User
from course.serializers import QuizSerializer, QuizProgressSerializer, LeaderBoardSerializer


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

    @action(detail=True, methods=['post'])
    def submit(self, request, pk):
        # Check if exist
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=pk)
        except Exception as e:
            raise e

        data = {"course": course.id, "user_id": user_id, "grade": request.data["grade"]}
        serializer = QuizProgressSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def leaderboard(self, request):
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
        except Exception as e:
            raise e

        progress = QuizProgress.objects.filter(user_id=user_id)
        course_ids = progress.values_list('course', flat=True)
        courses = CourseModel.objects.filter(id__in=course_ids)
        print(courses)

        return Response(LeaderBoardSerializer(courses, context={'user_id': user_id}, many=True).data)
