from course.views.course import CourseViewSet
from course.views.lesson import LessonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')
router.register(r'lesson', LessonViewSet, basename='lesson')
urlpatterns = router.urls
