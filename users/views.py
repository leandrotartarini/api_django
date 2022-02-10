from django.db import IntegrityError

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User


class UserRegistrationView(APIView):

    def get(self, request):
        try:
            user = User.objects.all()
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        try:
            user = User(email=request.data.get("email"))
            user.set_password(request.data.get("password"))
            user.save()
            return Response(status=status.HTTP_201_CREATED)

        except IntegrityError:
            pass
