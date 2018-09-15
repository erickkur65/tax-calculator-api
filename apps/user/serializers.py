from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from . import settings


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(min_length=5)
    password = serializers.CharField(min_length=5)


class RegistrationSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField(allow_blank=True)
    password = serializers.CharField(min_length=5)
    email = serializers.EmailField(validators=[
       UniqueValidator(
            queryset=User.objects.all(),
            message=settings.MSG_EMAIL_REGISTERED
       )
    ])

    def create(self, data):
        user = User.objects.create(**data)
        user.set_password(data['password'])
        user.save()

        return user
