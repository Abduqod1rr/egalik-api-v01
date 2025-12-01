from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['holat','title','kategoriya','tavsilot','narx','rasm','number','telegram']