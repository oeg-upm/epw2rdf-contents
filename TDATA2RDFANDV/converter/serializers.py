from rest_framework import serializers
from .models import downlEPW

class downlEPWSerializer(serializers.ModelSerializer):
    class Meta:
        model = downlEPW
        fields = '__all__'