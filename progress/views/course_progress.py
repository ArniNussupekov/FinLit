from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from progress.models import CourseProgress, LessonProgress
from course.models import CourseModel, LessonModel
from user.models import User

from progress.serializers import CourseProgressSerializer, LessonProgressSerializer, ListCourseProgressSerializer

from progress.tools.percent_progress import CalculatePercentage
from progress.tools.achievements import CalculateAchievements


class CourseProgressViewSet(viewsets.ViewSet):
    @classmethod
    def check_if_joined(cls, user_id, course_id):
        checker = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()

        print(checker)

        if checker is not None:
            print("YES")
            return True
        else:
            return False

    @classmethod
    def check_if_learned(cls, user_id, lesson_id):
        checker = LessonProgress.objects.filter(Q(lesson_id=lesson_id) & Q(user_id=user_id))

        if checker:
            return True
        else:
            return False

    def list(self, request):
        user_id = request.query_params.get("user_id")
        progress = CourseProgress.objects.filter(user_id=user_id)

        return Response(ListCourseProgressSerializer(progress, many=True).data)

    @action(detail=True, methods=['post'])
    def join(self, request, pk):

        # Todo make tool for checking user and course
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=pk)
        except Exception as e:
            raise e

        checker = self.check_if_joined(user.id, course.id)
        if checker is True:
            raise "User is already joined!"

        data = {"course_id": course.id, "user_id": user_id, "status": CourseProgress.Status.LEARNING,
                "course_level": course.module}

        serializer = CourseProgressSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        return Response({"Message": True})

    @action(detail=True, methods=['post'])
    def complete_lesson(self, request, pk):
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            lesson = LessonModel.objects.get(id=pk)
        except Exception as e:
            raise e

        checker = self.check_if_joined(user.id, lesson.course_id)
        lesson_checker = self.check_if_learned(user.id, lesson.id)

        if not checker:
            raise "You are not even joined the course!"
        elif lesson_checker:
            raise "You are completed course"

        try:
            course_progress = CourseProgress.objects.filter(Q(course_id=lesson.course_id) & Q(user_id=user_id)).first()
        except Exception as e:
            raise e

        data = {"user_id": user_id,
                "course_id": course_progress.course_id,
                "lesson_id": lesson.id,
                "course_progress": course_progress.id,
                "is_completed": True}

        serializer = LessonProgressSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        res = CalculatePercentage.calculate_percentage(course_progress.id)

        return Response({"message": res})

    @action(detail=False, methods=['get'])
    def get_achievements(self, request):
        user_id = request.query_params.get('user_id')

        completed_course = CalculateAchievements.calculate_completed_course(user_id=user_id)
        completed_modules = CalculateAchievements.calculate_complete_module(user_id=user_id)

        data = {"complete_courses": completed_course, "complete_modules": completed_modules}

        return Response(data)
