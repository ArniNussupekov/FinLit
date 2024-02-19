from django.shortcuts import render
from rest_framework import viewsets

from .models import CourseModel
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
