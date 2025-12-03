from django.shortcuts import render
from rest_framework.generics import CreateAPIView ,RetrieveUpdateDestroyAPIView , DestroyAPIView,RetrieveAPIView ,ListAPIView
from . import serializer
from .models import Products
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class AddProduct(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class=serializer.ProductSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    

class Home(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = serializer.ProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title']
    filterset_fields = ['kategoriya']  # TO'G'RI
    

class MyProducts(ListAPIView):
    serializer_class=serializer.ProductSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return Products.objects.filter(owner=self.request.user)
    

class productCrud(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = serializer.ProductSerializer
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
