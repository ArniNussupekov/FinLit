from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from progress.models import QuizProgress, CourseProgress
from course.models import CourseModel
from user.models import User

from progress.tools.percent_progress import CalculatePercentage


from progress.serializers import QuizProgressSerializer, LeaderBoardSerializer, CourseProgressSerializer
from user.serializers import UserSerializer


class QuizProgressViewSet(viewsets.ViewSet):
    @classmethod
    def complete_quiz(cls, user_id, course_id):
        try:
            progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        except Exception as e:
            raise "No such course in Progress"

        if progress.quiz_done:
            return Response({"Message:": "You have already submit"})

        data = {"quiz_done": True}
        serializer = CourseProgressSerializer(instance=progress, data=data, partial=True)
        serializer.is_valid()
        serializer.save()

        return progress.id

    @classmethod
    def get_course(cls, user_id, course_id):
        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=course_id)
        except Exception as e:
            raise e

        checker = QuizProgress.objects.filter(Q(course_id=course.id) & Q(user_id=user.id)).first()
        if checker:
            raise 'Quiz Submited'
        return course

    @classmethod
    def upgrade_balance(cls, user_id):
        user = User.objects.get(id=user_id)
        new_balance = user.balance + 25
        user_serializer = UserSerializer(instance=user, data={"balance": new_balance}, partial=True)
        user_serializer.is_valid()
        user_serializer.save()

    @action(detail=True, methods=['post'])
    def submit(self, request, pk):
        user_id = request.query_params.get("user_id")

        try:
            course = self.get_course(user_id=user_id, course_id=pk)
        except Exception:
            return Response({"AlreadySubmited": True})

        try:
            progress = CourseProgress.objects.filter(Q(course_id=pk) & Q(user_id=user_id)).first()
        except Exception as e:
            return Response({"NotJoinedCourse": True})

        self.upgrade_balance(user_id)

        grade = CalculatePercentage.calculate_grade(request.data["answers"])

        # Saving progress
        data = {"course_id": course.id, "user_id": user_id, "grade": grade, "user_choices": request.data["answers"]}
        serializer = QuizProgressSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        progress = self.complete_quiz(user_id, course.id)
        CalculatePercentage.calculate_percentage(progress)

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

    @action(detail=True, methods=['get'])
    def get_quiz_result(self, request, pk):
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
        except Exception as e:
            raise e

        progress = QuizProgress.objects.filter(Q(user_id=user_id) & Q(course_id=pk)).first()
        result = CalculatePercentage.get_quiz_result(progress)

        return Response({"result": result})
