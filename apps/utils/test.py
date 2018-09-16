from time import time

from django.contrib.auth import get_user_model
from model_mommy import mommy
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.test import APIJWTTestCase


class CustomerTestCase(APIJWTTestCase):
    def setUp(self):
        self.client = APIClient()
        self.guest_client = APIClient()

        # Get authorization from class attribute
        token = getattr(self, 'token', None)

        # Create dummy user and attach its token to header
        if not token:
            email = getattr(self, 'email', None)
            password = getattr(self, 'password', None)

            user = mommy.make(
                get_user_model(),
                username=f'user_{int(time())}'
            )

            user.email = email
            user.set_password(password)
            user.save()

            response = self.client.post(
                reverse('user:login'),
                data={'email': email, 'password': password},
                format='json'
            )
            token = response.data['token']

        self.client.credentials(HTTP_AUTHORIZATION='{} {}'.format(
            api_settings.JWT_AUTH_HEADER_PREFIX,
            token
        ))
