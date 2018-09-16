from rest_framework import serializers
from rest_framework.exceptions import ParseError

from tax import settings as tax_settings
from utils.generics import to_int
from . import settings as bill_settings
from .models import Bill, BillItem


class BillSerializer(serializers.Serializer):
    tax_items = serializers.JSONField()

    def create(self, data):
        if 'tax_items' not in data:
            raise ParseError(bill_settings.MSG_TAX_ITEMS_REQUIRED)

        bill_sub_total = 0
        bill_tax_total = 0
        bill_item_list = []

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
        bill_data = {}
        bill_data['user_id'] = self.context['request'].user.id
        bill_data['sub_total'] = bill_sub_total
        bill_data['tax_total'] = bill_tax_total
        bill_data['grand_total'] = bill_sub_total + bill_tax_total
        #bill = Bill.objects.create(**bill_data)

        # TODO:
        # Save bill items
        #bill.items.bulk_create(bill_item_list)
        print(bill_data)
        print(bill_item_list[1].qty)

        return bill


class BillItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillItem
