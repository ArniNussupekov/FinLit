from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from user.models import User
from user.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    @action(detail=False, methods=['post'], name="register")
    def register(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid()
        user_serializer.save()

        return Response({'success': True})

    @action(detail=False, methods=['post'], name="login")
    def login(self, request):
        try:
            user = User.objects.get(email=request.data["email"], password=request.data["password"])
        except Exception as e:
            return Response({"success:": False, "message": "Login or password not correct"})

        serializer = UserSerializer(user)
        return Response(serializer.data)
