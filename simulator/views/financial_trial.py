from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response

from simulator.models import FinancialTrialModel

from simulator.serializers import FinancialTrialSerializer


class FinancialTrialViewSet(viewsets.ViewSet):

    def list(self, request):
        level = request.query_params.get("Level")
        filters = {
            "stocks": request.query_params.get("stocks", None),
            "investment": request.query_params.get("investment", None),
            "money": request.query_params.get("money", None),
            "credit": request.query_params.get("credit", None),
            "economy": request.query_params.get("economy", None),
        }

        query = Q()
        for key, value in filters.items():
            if value:
                query |= Q(category=value)

        simulator = FinancialTrialModel.objects.filter(query)
        serializer = FinancialTrialSerializer(simulator, many=True)

        return Response(serializer.data)

    def create(self, request):
        serializer = FinancialTrialSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()

        return Response({"success": True, "data": serializer.data})

    def retrieve(self, request, pk):
        try:
            simulator = FinancialTrialModel.objects.get(id=pk)
        except Exception as e:
            raise "Object not found"
        serializer = FinancialTrialSerializer(simulator)

        return Response(serializer.data)

    def update(self, request, pk):
        course = FinancialTrialModel.objects.get(id=pk)
        serializer = FinancialTrialSerializer(instance=course, data=request.data, partial=True)
        serializer.is_valid()
        serializer.save()

        return Response({"Success": True, "data": serializer.data})

    def delete(self, request, pk):
        course = FinancialTrialModel.objects.get(id=pk)
        course.delete()

        return Response({"Success": True})