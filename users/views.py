import traceback

from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.serializers import UserSerializer


class UserView(APIView):

    def get(self, request):
        try:
            users = User.objects.all()
            serialized_users = UserSerializer(users, many=True).data

            return Response(serialized_users, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)


class UserViewDetail(APIView):

    def get(self, request, user_id: int):
        try:
            user = User.objects.get(id=user_id)
            serialized_user = UserSerializer(user).data
            return Response(serialized_user)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id: int):
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return Response({"message": "User removed successfully"})
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id: int):
        try:
            user = User.objects.get(id=user_id)
            user.email = request.data.get("email", user.email)
            user.password = request.data.get("password", user.password)
            user.save()
            serialized_user = UserSerializer(user).data
            return Response(serialized_user, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(traceback.format_exc())
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationView(APIView):

    def post(self, request):
        try:
            if len(request.data.get("password")) == 0:
                return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)

            user = User(email=request.data.get("email"))
            user.set_password(request.data.get("password"))
            user.save()
            serialized_user = UserSerializer(user).data
            return Response(serialized_user, status=status.HTTP_201_CREATED)

        except IntegrityError:
            print(traceback.format_exc())
            return Response({"message": "Error"}, status=status.HTTP_400_BAD_REQUEST)
