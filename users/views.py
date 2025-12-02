from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import userSerializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import UserCustomForm


class registerUser(CreateAPIView):
    serializer_class=userSerializers
    queryset=User.objects.all()

class loginUser(APIView):
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")

        user = authenticate(username=username,password=password)

        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({"message": f"Welcome {user.username} ✅"})
    

class logoutUser(APIView):
    def post(self,request):
        logout(request)
        return Response({"message": "Logged out successfully ✅"}, status=status.HTTP_200_OK)

    def get(self,request):
        logout(request)
        return Response({"message": "Logged out successfully ✅"}, status=status.HTTP_200_OK)