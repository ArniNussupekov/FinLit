from django.db.models import Q

from rest_framework import serializers
from .models import CourseModel, LessonModel, QuizModel, QuizAnswerModel, Accordion
from progress.models import CourseProgress, LessonProgress, QuizProgress
from user.models import User


class MyCoursesSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(method_name="get_status")
    progress = serializers.SerializerMethodField(method_name="get_progress")
    is_completed = serializers.SerializerMethodField(method_name="get_completed")
    lesson_num = serializers.SerializerMethodField(method_name="get_lesson_num")

    def get_lesson_num(self, course):
        try:
            course_id = course.id
            lessons_num = LessonModel.objects.filter(course_id=course_id).count()
        except Exception as e:
            raise e
        return lessons_num

    def get_status(self, course):
        try:
            user_id = self.context['user_id']
            course_id = course.id
            progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        except Exception as e:
            raise e
        if progress:
            return progress.status
        else:
            return None

    def get_progress(self, course):
        try:
            user_id = self.context['user_id']
            course_id = course.id
            progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        except Exception as e:
            raise e
        if progress:
            return progress.percent
        else:
            return None

    def get_completed(self, course):
        try:
            user_id = self.context['user_id']
            course_id = course.id
            progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        except Exception as e:
            raise e
        if progress:
            data = {"is_completed": progress.is_completed, "status": progress.status}
            return data
        else:
            return None

    class Meta:
        model = CourseModel
        fields = '__all__'


class BookmarkSerializer(serializers.ModelSerializer):
    progress = serializers.SerializerMethodField(method_name="get_progress")

    def get_progress(self, course):
        try:
            user_id = self.context['user_id']
            course_id = course.id
            progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        except Exception as e:
            raise e
        if progress:
            return progress.percent
        else:
            return 0

    class Meta:
        model = CourseModel
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'


class CourseRetrieveSerializer(serializers.ModelSerializer):
    is_bookmarked = serializers.SerializerMethodField(method_name="get_is_starred")
    is_completed = serializers.SerializerMethodField(method_name="get_is_completed")
    quiz_completed = serializers.SerializerMethodField(method_name="get_quiz_completed")
    grade = serializers.SerializerMethodField(method_name="get_grade")

    def get_is_starred(self, course):
        user_id = self.context['user_id']
        course_id = course.id
        user = User.objects.get(id=user_id)
        if user.bookmarked_courses.filter(id=course_id).exists():
            return True
        else:
            return False

    def get_is_completed(self, course):
        user_id = self.context['user_id']
        course_id = course.id
        progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        if progress:
            return progress.is_completed
        else:
            return False

    def get_quiz_completed(self, course):
        user_id = self.context['user_id']
        course_id = course.id
        progress = CourseProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        if progress:
            return progress.quiz_done
        else:
            return False

    def get_grade(self, course):
        user_id = self.context['user_id']
        course_id = course.id
        quiz_progress = QuizProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        if quiz_progress:
            return quiz_progress.grade
        else:
            return 0

    class Meta:
        model = CourseModel
        fields = '__all__'


class MyLessonSerializer(serializers.ModelSerializer):
    is_completed = serializers.SerializerMethodField(method_name="get_is_completed")
    accordions = serializers.SerializerMethodField(method_name='get_accordion')

    def get_accordion(self, lesson):
        accordions = Accordion.objects.filter(lesson=lesson.id)
        accordions_serializer = AccordionSerializer(accordions, many=True, read_only=True)

        return accordions_serializer.data

    def get_is_completed(self, lesson):
        user_id = self.context['user_id']
        lesson_id = lesson.id
        lesson_progress = LessonProgress.objects.filter(Q(user_id=user_id) & Q(lesson_id=lesson_id)).first()
        try:
            return lesson_progress.is_completed
        except Exception as e:
            return False

    class Meta:
        model = LessonModel
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonModel
        fields = '__all__'


class AccordionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accordion
        fields = '__all__'


class RetrieveLessonSerializer(serializers.ModelSerializer):
    accordions = serializers.SerializerMethodField(method_name='get_accordion')

    def get_accordion(self, lesson):
        accordions = Accordion.objects.filter(lesson=lesson.id)
        accordions_serializer = AccordionSerializer(accordions, many=True, read_only=True)

        return accordions_serializer.data

    class Meta:
        model = LessonModel
        fields = ['lesson_num', 'name', 'description', 'url', 'course', 'accordions']


class QuizAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAnswerModel
        fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(method_name="get_answers")

    def get_answers(self, quiz):
        answers = QuizAnswerModel.objects.filter(quiz_id=quiz.id)
        serializer = QuizAnswerSerializer(answers, many=True, read_only=True)

        return serializer.data

    class Meta:
        model = QuizModel
        fields = ['id', 'course_id', 'question', 'answers']


class QuizHistorySerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField(method_name="get_answers")
    feedback_sent = serializers.SerializerMethodField(method_name='get_feedback_sent')

    def get_feedback_sent(self, quiz):
        return True

    def get_answers(self, quiz):
        user_id = self.context['user_id']
        course_id = quiz.course_id
        answers = QuizAnswerModel.objects.filter(quiz_id=quiz.id)
        serializer = QuizAnswerSerializer(answers, many=True, read_only=True)

        quiz_progress = QuizProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id)).first()
        chosen = list(quiz_progress.user_choices)

        for answer in serializer.data:
            if answer['id'] in chosen:
                answer['chosen'] = True
            else:
                answer['chosen'] = False

        return serializer.data

    class Meta:
        model = QuizModel
        fields = ['id', 'course_id', 'question', 'answers', 'feedback_sent']
