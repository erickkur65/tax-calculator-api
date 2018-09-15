import json

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse


class CustomerRegister(TestCase):
    def test_register_success(self):
        post_data = {
            'first_name': 'test',
            'last_name': '123',
            'email': 'test@gmail.com',
            'password': 'test123'
        }

        response = self.client.post(
            reverse('user:register'),
            data=json.dumps(post_data),
            content_type='application/json'
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
