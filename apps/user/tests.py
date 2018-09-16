from rest_framework import status
from rest_framework.reverse import reverse

from utils.test import CustomerTestCase


class CustomerRegister(CustomerTestCase):
    email = 'test@gmail.com'
    password = 'test123'

    def test_register_success(self):
        post_data = {
            'first_name': 'test',
            'last_name': '123',
            'email': 'test2@gmail.com',
            'password': 'test123'
        }

        response = self.client.post(
            reverse('user:register'),
            data=post_data,
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_register_fail(self):
        post_data = {
            'first_name': 'test',
            'last_name': '123',
            'email': self.email,
            'password': self.password
        }

        response = self.client.post(
            reverse('user:register'),
            data=post_data,
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)


class CustomerLogin(CustomerTestCase):
    email = 'test@gmail.com'
    password = 'test123'

    def test_login_success(self):
        post_data = {
            'email': self.email,
            'password': self.password
        }

        response = self.client.post(
            reverse('user:login'),
            data=post_data,
            format='json'
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_login_fail(self):
        post_data = {
            'email': self.email,
            'password': 'wrong password'
        }

        response = self.client.post(
            reverse('user:login'),
            data=post_data,
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
