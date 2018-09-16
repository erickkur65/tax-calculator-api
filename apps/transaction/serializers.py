from rest_framework import serializers
from rest_framework.exceptions import ParseError

from tax import settings as tax_settings
from tax.serializers import TaxItemSerializer
from utils.generics import to_int
from . import settings as bill_settings
from .models import Bill, BillItem


class BillSerializer(serializers.Serializer):
    sub_total = serializers.DecimalField(
        max_digits=16,
        decimal_places=4,
        read_only=True
    )
    tax_total = serializers.DecimalField(
        max_digits=16,
        decimal_places=4,
        read_only=True
    )
    grand_total = serializers.DecimalField(
        max_digits=16,
        decimal_places=4,
        read_only=True
    )
    bill_items = serializers.SerializerMethodField(read_only=True)
    tax_items = serializers.JSONField(write_only=True)

    def get_bill_items(self, obj):
        bill_items = BillItem.objects.filter(bill_id=obj.id)
        serializer = BillItemSerializer(bill_items, many=True)

        return serializer.data

    def create(self, data):
        if 'tax_items' not in data:
            raise ParseError(bill_settings.MSG_TAX_ITEMS_REQUIRED)

        # Initialize bill and bill item data
        bill_data = {}
        bill_sub_total = 0
        bill_tax_total = 0
        bill_item_list = []

        # Save bill object to use for foreign key in bill item object
        bill_data['user_id'] = self.context['request'].user.id
        bill = Bill.objects.create(**bill_data)

        for tax_item in data['tax_items']:
            order_amount = to_int(tax_item.get('qty')) * to_int(tax_item.get('amount'))
            tax_amount = 0

            # Calculate tax amount
            if tax_item.get('tax_code') == tax_settings.TAX_CODE_FOOD:
                tax_amount = 0.1 * order_amount
            elif tax_item.get('tax_code') == tax_settings.TAX_CODE_TOBACCO:
                tax_amount = 10 + (0.02 * order_amount)
            elif tax_item.get('tax_code') == tax_settings.TAX_CODE_ENTERTAINMENT:
                if order_amount > 100:
                    tax_amount = 0.01 * (order_amount - 100)

            # Assign data for bill item
            total_amount = order_amount + tax_amount
            bill_item = BillItem(
                bill=bill,
                qty=tax_item.get('qty'),
                tax_item_id=tax_item.get('tax_item_id'),
                tax_amount=tax_amount,
                total_amount=total_amount
            )
            bill_item_list.append(bill_item)

            # Calculate sub_total, tax_total for bill
            bill_sub_total += order_amount
            bill_tax_total += tax_amount

        # Assign and save data for bill
        bill.sub_total = bill_sub_total
        bill.tax_total = bill_tax_total
        bill.grand_total = bill_sub_total + bill_tax_total
        bill.save()

        # Save bill items for current bill
        bill.items.bulk_create(bill_item_list)

        return bill


class BillItemSerializer(serializers.ModelSerializer):
    qty = serializers.IntegerField()
    tax_amount = serializers.DecimalField(max_digits=16, decimal_places=4)
    total_amount = serializers.DecimalField(max_digits=16, decimal_places=4)
    tax_item = TaxItemSerializer(read_only=True)

    class Meta:
        model = BillItem
        fields = ('id', 'qty', 'tax_amount', 'total_amount', 'tax_item')
