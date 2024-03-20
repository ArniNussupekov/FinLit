from progress.views.quiz_progress import QuizProgressViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'quiz_progress', QuizProgressViewSet, basename='quiz_progress')
urlpatterns = router.urls
