from rest_framework import serializers
from .models import Bill, BillItem


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill


class BillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillItem
