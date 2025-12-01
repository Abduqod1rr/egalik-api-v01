from django.shortcuts import render
from rest_framework.generics import CreateAPIView ,RetrieveUpdateDestroyAPIView , DestroyAPIView,RetrieveAPIView ,ListAPIView
from . import serializer
from .models import Products


class AddProduct(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class=serializer.ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    

class Home(ListAPIView):
    queryset=Products.objects.all()
    serializer_class=serializer.ProductSerializer
    

    
    

