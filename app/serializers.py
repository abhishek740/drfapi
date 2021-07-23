from rest_framework import fields, serializers
from .models import *

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Producterializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        