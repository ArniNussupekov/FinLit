from user.auth.auth import UserViewSet
from user.profile.profile import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'auth', UserViewSet, basename='register')
router.register(r'auth', UserViewSet, basename='login')
router.register(r'profile', ProfileViewSet, basename='profile')
urlpatterns = router.urls
