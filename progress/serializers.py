from django.db.models import Q

from rest_framework import serializers

from progress.models import QuizProgress, CourseProgress, LessonProgress
from course.models import CourseModel


class LessonProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonProgress
        fields = '__all__'


class ListCourseProgressSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField(method_name="get_course_name")
    course_level = serializers.SerializerMethodField(method_name="get_course_level")

    def get_course_level(self, course_progress):
        course = CourseModel.objects.get(id=course_progress.course_id)

        return course.module

    def get_course_name(self, course_progress):
        course = CourseModel.objects.get(id=course_progress.course_id)

        return course.name

    class Meta:
        model = CourseProgress
        fields = '__all__'


class CourseProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseProgress
        fields = '__all__'


class QuizProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizProgress
        fields = '__all__'


class LeaderBoardSerializer(serializers.ModelSerializer):
    grade = serializers.SerializerMethodField(method_name="get_grade")

    def get_grade(self, course):
        user_id = self.context['user_id']
        course_id = course.id
        progress = QuizProgress.objects.filter(Q(user_id=user_id) & Q(course_id=course_id)).first()
        the_progress = progress.get(course_id=course_id)

        return the_progress.grade

    class Meta:
        model = CourseModel
        fields = ['id', 'name', 'category', 'course_num', 'module', 'grade']
