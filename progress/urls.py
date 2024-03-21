from progress.views.quiz_progress import QuizProgressViewSet
from progress.views.course_progress import CourseProgressViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'quiz_progress', QuizProgressViewSet, basename='quiz_progress')
router.register(r'course_progress', CourseProgressViewSet, basename='course_progress')
urlpatterns = router.urls
