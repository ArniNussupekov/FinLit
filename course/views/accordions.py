from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from course.models import Accordion
from course.serializers import AccordionSerializer


class AccordionViewSet(viewsets.ViewSet):

    def list(self, request):
        accordions = Accordion.objects.all()

        serializer = AccordionSerializer(accordions, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = AccordionSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"success": True, "data": serializer.data})

    def retrieve(self, request, pk):
        try:
            quiz = Accordion.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        return Response(AccordionSerializer(quiz).data)

    def update(self, request, pk):
        try:
            accordion = Accordion.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        serializer = AccordionSerializer(instance=accordion, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response({"message": True, "data": serializer.data})

    def delete(self, request, pk):
        try:
            accordion = Accordion.objects.get(id=pk)
        except Exception as e:
            raise "Not Found"

        accordion.delete()
        return Response({"message": True})
