from rest_framework import serializers
from .models import CallDetailRecord

class CallDetailRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallDetailRecord
        fields = '__all__'
