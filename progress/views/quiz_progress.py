from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from progress.models import QuizProgress
from course.models import CourseModel
from user.models import User


from progress.serializers import QuizProgressSerializer, LeaderBoardSerializer


class QuizProgressViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['post'])
    def submit(self, request, pk):
        # Check if exist
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=pk)
        except Exception as e:
            raise e

        checker = QuizProgress.objects.filter(Q(course=course.id) & Q(user_id=user.id))
        if checker:
            raise "QuizProgress is already exists!"

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