from django.urls import path
from certificate.views import my_view

urlpatterns = [
    path('my_page/', my_view, name='my_page'),
]
