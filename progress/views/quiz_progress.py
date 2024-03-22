from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from progress.models import QuizProgress, CourseProgress
from course.models import CourseModel
from user.models import User


from progress.serializers import QuizProgressSerializer, LeaderBoardSerializer, CourseProgressSerializer


class QuizProgressViewSet(viewsets.ViewSet):
    @classmethod
    def complete_course(cls, user_id, course_id):
        try:
            progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        except Exception as e:
            raise "No such course in Progress"

        data = {"is_completed": True}
        serializer = CourseProgressSerializer(instance=progress, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        print(serializer.is_valid())
        return True

    @classmethod
    def get_course(cls, user_id, course_id):
        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=course_id)
        except Exception as e:
            raise e

        checker = QuizProgress.objects.filter(Q(course_id=course.id) & Q(user_id=user.id))
        if checker:
            raise "QuizProgress is already exists!"
        return course

    @action(detail=True, methods=['post'])
    def submit(self, request, pk):
        user_id = request.query_params.get("user_id")
        course = self.get_course(user_id=user_id, course_id=pk)

        data = {"course_id": course.id, "user_id": user_id, "grade": request.data["grade"]}
        serializer = QuizProgressSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        self.complete_course(user_id, course.id)

        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def leaderboard(self, request):
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
        except Exception as e:
            raise e

        progress = QuizProgress.objects.filter(user_id=user_id)
        course_ids = progress.values_list('course_id', flat=True)
        courses = CourseModel.objects.filter(id__in=course_ids)

        return Response(LeaderBoardSerializer(courses, context={'user_id': user_id}, many=True).data)