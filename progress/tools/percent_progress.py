from django.db.models import Q

from progress.models import LessonProgress, QuizProgress, CourseProgress
from course.models import LessonModel

from progress.serializers import CourseProgressSerializer


class CalculatePercentage:
    @classmethod
    def calculate_lesson_percentage(cls, user_id, course_id):
        lessons = LessonProgress.objects.filter(Q(course_id=course_id) & Q(user_id=user_id))
        lesson_num = LessonModel.objects.count()
        max_fill = 70
        complete = lessons.count()
        fill = (100 * complete) / lesson_num
        percentage = (max_fill * fill) / 100

        return percentage

    @classmethod
    def calculate_quiz_percentage(cls, course_progress):
        if course_progress.is_completed:
            return 30
        else:
            return 0

    @classmethod
    def calculate_percentage(cls, course_progress_id):
        course_progress = CourseProgress.objects.get(id=course_progress_id)
        lesson_percent = cls.calculate_lesson_percentage(course_progress.user_id, course_progress.course_id)
        quiz_percent = cls.calculate_quiz_percentage(course_progress)

        data = {"percent": lesson_percent+quiz_percent}
        serializer = CourseProgressSerializer(instance=course_progress, data=data, partial=True)
        serializer.is_valid()
        serializer.save()
        return data
