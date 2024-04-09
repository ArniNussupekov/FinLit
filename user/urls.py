from user.auth.auth import RegisterView, LoginView, UserView, LogoutView
from user.profile.profile import ProfileViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('active_user/', UserView.as_view()),
    path('logout/', LogoutView.as_view()),
]

urlpatterns += router.urls

