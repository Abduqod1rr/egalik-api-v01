from django.shortcuts import render
from rest_framework.generics import CreateAPIView ,RetrieveUpdateDestroyAPIView , DestroyAPIView,RetrieveAPIView ,ListAPIView
from . import serializer
from .models import Products
from rest_framework.permissions import IsAuthenticated


class AddProduct(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class=serializer.ProductSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    

class Home(ListAPIView):
    queryset=Products.objects.all()
    serializer_class=serializer.ProductSerializer
    

    
    

