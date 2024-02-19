from course.views import CourseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CourseViewSet, basename='course')
urlpatterns = router.urls
