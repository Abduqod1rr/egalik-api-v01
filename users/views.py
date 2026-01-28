from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import userSerializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , permissions
from .forms import UserCustomForm
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()  # blacklist the refresh token
            return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


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
    
