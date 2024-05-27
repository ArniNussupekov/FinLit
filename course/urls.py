from course.views.course import CourseViewSet
from course.views.lesson import LessonViewSet
from course.views.quiz import QuizViewSet
from course.views.feedback import CourseFeedbackViewSet
from course.views.accordions import AccordionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'lesson', LessonViewSet, basename='lesson')
router.register(r'quiz', QuizViewSet, basename='quiz')
router.register(r'feedback', CourseFeedbackViewSet, basename='feedback')
router.register(r'accordion', AccordionViewSet, basename='accordion')
urlpatterns = router.urls
