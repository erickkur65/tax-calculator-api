from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(min_length=5)
    password = serializers.CharField(min_length=5)
