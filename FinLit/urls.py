from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('course.urls')),
    path('user/', include('user.urls')),
    path('administrator/', include('administrator.urls')),
    path('progress/', include('progress.urls')),
]
