from rest_framework import serializers
from .models import ApiTest

class APISerializer(serializers.ModelSerializer):

    class Meta:
        model = ApiTest
        fields = '__all__'
