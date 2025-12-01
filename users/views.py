from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializer import userSerializers
from django.contrib.auth.models import User

class registerUser(CreateAPIView):
    serializer_class=userSerializers
    queryset=User.objects.all()
    