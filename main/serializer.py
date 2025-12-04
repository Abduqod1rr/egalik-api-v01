from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Products
        fields = ['id','owner','holat','title','kategoriya','tavsilot','narx','rasm','number','telegram']
        read_only_fields = ['id', 'owner']