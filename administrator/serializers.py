from rest_framework import serializers

from course.models import CourseModel, LessonModel, QuizModel, QuizAnswerModel


class AdminCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'


class AdminLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = '__all__'


class AdminQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = '__all__'


class AdminQuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswerModel
        fields = '__all__'
