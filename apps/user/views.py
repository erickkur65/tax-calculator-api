from rest_framework import generics, status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from utils.serializers import validate
from . import settings
from .helpers import EmailModelBackend
from .serializers import LoginSerializer, RegistrationSerializer


class Login(generics.CreateAPIView):
    """
    post:
    Make user login
    """
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        validate(serializer)

        user = EmailModelBackend().authenticate(
            request,
            email=serializer.data['email'],
            password=serializer.data['password']
        )

        if user is None:
            raise ParseError(settings.MSG_EMAIL_PASSWORD_INVALID)

        return _generate_token_response(user)


class Register(generics.CreateAPIView):
    """
    post:
    Create new user
    """
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        validate(serializer)
        user = serializer.save()

        return _generate_token_response(user)


def _generate_token_response(user):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    return Response(
        data={'token': token},
        status=status.HTTP_200_OK
    )
