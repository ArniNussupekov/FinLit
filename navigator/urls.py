from navigator.views.orientation_test import QuizViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'orientation_test', QuizViewSet, basename='orientation_test')
urlpatterns = router.urls
