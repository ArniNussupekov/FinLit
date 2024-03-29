from administrator.views.course import AdminCourseViewSet
from administrator.views.lesson import AdminLessonViewSet
from administrator.views.quiz import AdminQuizViewSet
from administrator.views.quiz_answer import AdminQuizAnswerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'course', AdminCourseViewSet, basename='course')
router.register(r'lesson', AdminLessonViewSet, basename='lesson')
router.register(r'quiz', AdminQuizViewSet, basename='quiz')
router.register(r'quiz_answer', AdminQuizAnswerViewSet, basename='quiz_answer')
urlpatterns = router.urls
