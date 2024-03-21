from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from course.models import CourseModel
from progress.models import CourseProgress

from progress.serializers import CourseProgressSerializer


class CourseFeedbackViewSet(viewsets.ViewSet):
    def get_progress(self, user_id, course_id):
        try:
            user = User.objects.get(id=user_id)
            course = CourseModel.objects.get(id=course_id)
            progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        except Exception as e:
            raise e

        if progress:
            return progress
        else:
            raise "No such progress"

    def calculate_feedback(self, new_feedback, pk):
        course = CourseModel.objects.get(id=pk)
        course.votes_sum += float(new_feedback)
        course.votes += 1
        try:
            course.rating = (course.votes_sum / course.votes)
        except Exception as e:
            raise e
        course.save()

        return course.rating

    @action(detail=True, methods=['put'])
    def send_feedback(self, request, pk):
        user_id = request.query_params.get("user_id")
        progress = self.get_progress(user_id, pk)

        serializer = CourseProgressSerializer(instance=progress, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        updated_rating = self.calculate_feedback(request.data["rating"], pk)

        return Response({"updated_rating": updated_rating})

    def retrieve(self, request, pk):
        user_id = request.query_params.get("user_id")

        try:
            progress = CourseProgress.objects.filter(Q(course_id=pk) & Q(user_id=user_id)).first()
        except Exception as e:
            raise e

        return Response(CourseProgressSerializer(progress).data)
