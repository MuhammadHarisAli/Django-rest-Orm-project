from rest_framework import serializers

from .models import DataSetModel

class DataSetSerializer(serializers.Serializer):
    class Meta:
        model = DataSetModel
