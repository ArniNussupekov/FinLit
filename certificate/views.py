from django.shortcuts import render
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CertificateViewSet(viewsets.ViewSet):
   @action(detail=False, methods=['get'])
   def my_page(self, request):
       name = "My Name"

       return render(request, 'index.html', {'name': name})
