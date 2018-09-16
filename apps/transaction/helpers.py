from tax.models import TaxItem


def check_tax_item_exist(data):
    for item in data['tax_items']:
        try:
            TaxItem.objects.get(pk=item.get('tax_item_id'))
        except TaxItem.DoesNotExist:
            return False

    return True
