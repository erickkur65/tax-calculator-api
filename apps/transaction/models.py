from django.db import models

from utils.models import BaseModel


class Bill(BaseModel):
    user = models.ForeignKey(
        'user.User',
        related_name='bills',
        on_delete=models.CASCADE)
    sub_total = models.DecimalField(
        max_digits=16,
        decimal_places=4,
        blank=True,
        null=True)
    tax_total = models.DecimalField(
        max_digits=16,
        decimal_places=4,
        blank=True,
        null=True)
    grand_total = models.DecimalField(
        max_digits=16,
        decimal_places=4,
        blank=True,
        null=True)


class BillItem(BaseModel):
    bill = models.ForeignKey(
        'transaction.Bill',
        related_name='items',
        on_delete=models.CASCADE)
    qty = models.IntegerField(null=True)
    tax_item = models.ForeignKey(
        'tax.TaxItem',
        related_name='bill_items',
        on_delete=models.CASCADE)
    tax_amount = models.DecimalField(
        max_digits=16,
        decimal_places=4,
        null=True)
    total_amount = models.DecimalField(
        max_digits=16,
        decimal_places=4,
        null=True)
