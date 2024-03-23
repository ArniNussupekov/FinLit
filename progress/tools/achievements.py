from django.db.models import Q

from progress.models import LessonProgress, CourseProgress
from course.models import CourseModel

from progress.serializers import CourseProgressSerializer


class CalculateAchievements:
    # ToDo Optimize
    @classmethod
    def calculate_complete_module(cls, user_id):
        completed_first = CourseProgress.objects.filter(Q(user_id=user_id) & Q(is_completed=False)
                                                        & Q(course_level=1))
        completed_second = CourseProgress.objects.filter(Q(user_id=user_id) & Q(is_completed=False)
                                                        & Q(course_level=2))
        completed_third = CourseProgress.objects.filter(Q(user_id=user_id) & Q(is_completed=False)
                                                        & Q(course_level=3))
        completed_modules = 0

        if not completed_first and CourseProgress.objects.filter(Q(user_id=user_id) & Q(is_completed=True)
                                                                 & Q(course_level=1)):
            completed_modules += 1
        
        if not completed_second and CourseProgress.objects.filter(Q(user_id=user_id) & Q(is_completed=True)
                                                        & Q(course_level=2)):
            completed_modules += 1

        if not completed_third and CourseProgress.objects.filter(Q(user_id=user_id) & Q(is_completed=True)
                                                        & Q(course_level=3)):
            completed_modules +=1

        return completed_modules

    @classmethod
    def calculate_completed_course(cls, user_id):
        completed = CourseProgress.objects.filter(Q(user_id=user_id) & Q(is_completed=True)).count()

        return completed
