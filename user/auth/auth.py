import uuid
from datetime import timedelta
from django.utils.timezone import now

from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User, EmailVerification
from user.serializers import UserSerializer

import jwt, datetime


class RegisterView(APIView):
    def post(self, request):
        unicode = 35

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user = User.objects.get(id=serializer.data["id"])
        new_code = int(str(unicode) + str(serializer.data["id"]))
        serializer = UserSerializer(instance=user, data={"unicode": new_code}, partial=True)
        serializer.is_valid()
        serializer.save()

        expiration = now() + timedelta(minutes=50)
        record = EmailVerification.objects.create(user=user, code=uuid.uuid4(), expiration=expiration)

        message_content = {
            "title": "FinLit Email Confirmation",
            "message": f"Good day! Here is unicode to confirm your email: {user.unicode}"
        }

        record.send_verification_email(message_content)

        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response({"message": "No such user"})

        if not user.check_password(password):
            return Response({"message": "Incorrect password"})

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            return Response({"message": "Unauthenticated"})

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({"message": "Unauthenticated"})

        user = User.objects.get(id=payload['id'])
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'Success'
        }

        return response
