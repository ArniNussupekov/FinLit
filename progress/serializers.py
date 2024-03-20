from rest_framework import serializers

from progress.models import QuizProgress
from course.models import CourseModel


class QuizProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizProgress
        fields = '__all__'


class LeaderBoardSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField(method_name="get_grade")

    def get_grade(self, course):
        user_id = self.context['user_id']
        course_id = course.id
        progress = QuizProgress.objects.filter(user_id=user_id)
        the_progress = progress.get(course=course_id)

        return the_progress.grade

    class Meta:
        model = CourseModel
        fields = ['id', 'name', 'category', 'course_num', 'module', 'grade']
