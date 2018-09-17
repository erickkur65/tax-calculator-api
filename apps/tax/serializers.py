from rest_framework import serializers
from rest_framework.exceptions import ParseError

from .models import TaxItem
from . import settings


class TaxItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(min_length=3)
    tax_code = serializers.IntegerField()
    amount = serializers.DecimalField(max_digits=16, decimal_places=4)

    class Meta:
        model = TaxItem
        fields = ('id', 'name', 'tax_code', 'amount')

    def create(self, data):
        tax_type = ''
        list_tax_code = [
            settings.TAX_CODE_FOOD,
            settings.TAX_CODE_TOBACCO,
            settings.TAX_CODE_ENTERTAINMENT]

        # Validate tax code must be exist
        if data['tax_code'] not in list_tax_code:
            raise ParseError(settings.MSG_TAX_CODE_REGISTERED)

        # Validate tax name must unique
        if TaxItem.objects.filter(name=data['name']):
            raise ParseError(settings.MSG_TAX_NAME_MUST_UNIQUE)

        # Calculate tax amount according tax code
        if data['tax_code'] == settings.TAX_CODE_FOOD:
            tax_type = settings.TAX_TYPE_FOOD
        elif data['tax_code'] == settings.TAX_CODE_TOBACCO:
            tax_type = settings.TAX_TYPE_TOBACCO
        elif data['tax_code'] == settings.TAX_CODE_ENTERTAINMENT:
            tax_type = settings.TAX_TYPE_ENTERTAINMENT

        data['tax_type'] = tax_type
        tax_item = TaxItem.objects.create(**data)

        return tax_item
