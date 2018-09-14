from django.db import models

from utils.models import BaseModel


class TaxItem(BaseModel):
    name = models.CharField(max_length=64)
    tax_code = models.SmallIntegerField()
    tax_type = models.CharField(max_length=20)
    amount = models.DecimalField(
        max_digits=16,
        decimal_places=4)
    tax_amount = models.DecimalField(
        max_digits=16,
        decimal_places=4)
    total_amount = models.DecimalField(
        max_digits=16,
        decimal_places=4)
