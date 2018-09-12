from django.contrib.auth.models import AbstractUser
from django.db import models


class Customer(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=True,
        default=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_email = self.email
