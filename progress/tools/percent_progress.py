from django.db.models import Q

from progress.models import LessonProgress, CourseProgress
from course.models import LessonModel, QuizAnswerModel

from progress.serializers import CourseProgressSerializer


class CalculatePercentage:
    @classmethod
    def calculate_grade(cls, data):
        quiz_answers = QuizAnswerModel.objects.filter(id__in=data)
        answer_count = quiz_answers.count()
        correct_answer_num = 0

        for answer in quiz_answers:
            if answer.is_correct is True:
                correct_answer_num += 1

        percent = (float(correct_answer_num/answer_count)) * 100

        return percent

    @classmethod
    def calculate_lesson_percentage(cls, user_id, course_id):
        lessons = LessonProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id))
        lesson_num = LessonModel.objects.filter(course_id=course_id).count()
        max_fill = 70
        complete = lessons.count()
        fill = (100 * complete) / lesson_num
        percentage = (max_fill * fill) / 100

        return percentage

    @classmethod
    def calculate_quiz_percentage(cls, course_progress):
        if course_progress.quiz_done:
            return 30
        else:
            return 0

    @classmethod
    def complete_course(cls, lesson_percent, quiz_percent):
        total = lesson_percent+quiz_percent
        if total == 100:
            return True
        else:
            return False

    @classmethod
    def calculate_percentage(cls, course_progress_id):
        course_progress = CourseProgress.objects.get(id=course_progress_id)
        lesson_percent = cls.calculate_lesson_percentage(course_progress.user_id, course_progress.course_id)
        quiz_percent = cls.calculate_quiz_percentage(course_progress)
        completed = cls.complete_course(lesson_percent, quiz_percent)

        if completed:
            status = CourseProgress.Status.COMPLETED
        else:
            status = CourseProgress.Status.LEARNING

        data = {"percent": lesson_percent+quiz_percent, "is_completed": completed, "status": status}
        serializer = CourseProgressSerializer(instance=course_progress, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        return data
