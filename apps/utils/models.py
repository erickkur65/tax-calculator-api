from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class GeneralManager(models.Manager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except ObjectDoesNotExist:
            return None


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = GeneralManager()

    class Meta:
        abstract = True
