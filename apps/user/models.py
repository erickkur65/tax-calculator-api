import time

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        null=True,
        default=None)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_email = self.email

    def full_name(self):
        if not self.first_name:
            return self.username

        full_name = self.first_name
        if self.last_name:
            full_name += ' ' + self.last_name

        return full_name

    def save(self, *args, **kwargs):
        # Build username
        if not self.username:
            unix_time = int(time.time())
            full_name = self.full_name().replace(' ', '_')
            self.username = f'{full_name}_{unix_time}'

        super().save(*args, **kwargs)
