from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from usermanagement.serializer import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

class UserManagement(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format = None):
        user = User.objects.all()
        serializer = UserSerializer(user, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format = None):
        username = request.data["username"]
        password = request.data["password"]
        email = request.data["email"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        try:
            user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
            user.save()
            Token.objects.get_or_create(user = user)
            return Response({"credentials" : "saved"}, status = status.HTTP_201_CREATED)
        except:
            return Response({"credentials" : "already exist"}, status = status.HTTP_200_OK)