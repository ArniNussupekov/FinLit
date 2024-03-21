from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from progress.models import CourseProgress
from course.models import CourseModel, LessonModel
from user.models import User

from progress.serializers import CourseProgressSerializer, LessonProgressSerializer


class CourseProgressViewSet(viewsets.ViewSet):
    def check_if_joined(self, user_id, course_id):
        checker = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id))

        if checker:
            return True
        else:
            return False

    @action(detail=True, methods=['post'])
    def join(self, request, pk):

        # Todo make tool for checking user and course
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=pk)
        except Exception as e:
            raise e

        checker = self.check_if_joined(course.id, user.id)
        if checker:
            raise "User is already joined!"

        data = {"course_id": course.id, "user_id": user_id, "status": CourseProgress.Status.LEARNING}
        print(data)
        serializer = CourseProgressSerializer(data=data)
        serializer.is_valid()
        serializer.save()

        return Response({"Message": True})

    @action(detail=True, methods=['post'])
    def complete_course(self, request, pk):
        pass

    @action(detail=True, methods=['post'])
    def complete_lesson(self, request, pk):
        user_id = request.query_params.get("user_id")
        try:
            user = User.objects.get(id=user_id)
            lesson = LessonModel.objects.get(id=pk)
        except Exception as e:
            raise e

        checker = self.check_if_joined(user.id, lesson.course_id)

        if not checker:
            raise "You are not even joined the course!"

        data = {"user_id": user_id,
                "lesson_id": lesson.id,
                "course_progress": CourseProgress.objects.get(course_id=lesson.course_id),
                "is_completed": True}

        serializer = LessonProgressSerializer(data=data)
        serializer.is_valid()
        serializer.save()
