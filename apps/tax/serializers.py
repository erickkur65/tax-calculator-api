from rest_framework import serializers
from .models import TaxItem


class TaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxItem
