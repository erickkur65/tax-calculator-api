from rest_framework import serializers
from rest_framework.exceptions import ParseError
from rest_framework.validators import UniqueValidator

from .models import TaxItem
from . import settings


class TaxSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3)
    tax_code = serializers.IntegerField()
    amount = serializers.IntegerField()

    class Meta:
        model = TaxItem
        fields = ('id', 'name', 'tax_code', 'amount')

    def create(self, data):
        tax_amount = 0
        tax_type = ''
        list_tax_code = [
            settings.TAX_CODE_FOOD,
            settings.TAX_CODE_TOBACCO,
            settings.TAX_CODE_ENTERTAINMENT]

        # Validate tax code must be exist
        if data['tax_code'] not in list_tax_code:
            raise ParseError(settings.MSG_TAX_CODE_REGISTERED)

        # Calculate tax amount according tax code
        if data['tax_code'] == settings.TAX_CODE_FOOD:
            tax_type = settings.TAX_TYPE_FOOD
            tax_amount = 0.1 * data['amount']
        elif data['tax_code'] == settings.TAX_CODE_TOBACCO:
            tax_type = settings.TAX_TYPE_TOBACCO
            tax_amount = 10 + (0.02 * data['amount'])
        elif data['tax_code'] == settings.TAX_CODE_ENTERTAINMENT:
            if data['amount'] > 100:
                tax_type = settings.TAX_TYPE_ENTERTAINMENT
                tax_amount = 0.01 * (data['amount'] - 100)

        data['tax_type'] = tax_type
        data['tax_amount'] = tax_amount
        data['total_amount'] = data['amount'] + data['tax_amount']
        tax_item = TaxItem.objects.create(**data)

        return tax_item
