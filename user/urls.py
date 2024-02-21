from django.urls import path, include

from user.auth.auth import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', UserViewSet, basename='register')
router.register(r'', UserViewSet, basename='login')
urlpatterns = router.urls
