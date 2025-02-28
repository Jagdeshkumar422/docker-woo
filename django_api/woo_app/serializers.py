from rest_framework import serializers
from .model import ProductMetaLookup

class ProductMetaLookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMetaLookup
        fields = '__all__'  # Include all fields
