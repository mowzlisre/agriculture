from dataclasses import fields
from rest_framework import serializers
from .models import *

class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'