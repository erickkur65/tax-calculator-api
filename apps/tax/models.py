from django.db import models

from utils.models import BaseModel


class TaxItem(BaseModel):
    name = models.CharField(
        max_length=64,
        blank=True,
        null=True)
    tax_code = models.SmallIntegerField()
    amount = models.DecimalField(
        max_digits=16,
        decimal_places=4,
        blank=True,
        null=True)
    tax_amount = models.DecimalField(
        max_digits=16,
        decimal_places=4,
        blank=True,
        null=True)
    total_amount = models.DecimalField(
        max_digits=16,
        decimal_places=4,
        blank=True,
        null=True)
