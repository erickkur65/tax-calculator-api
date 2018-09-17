from decimal import Decimal

from model_mommy import mommy
from rest_framework import status
from rest_framework.reverse import reverse

from . import settings
from tax.models import TaxItem
from utils.test import CustomerTestCase


class TaxItemTest(CustomerTestCase):
    email = 'test@gmail.com'
    password = 'test123'

    def test_create_new_tax_item(self):
        data = {
            'name': 'food 1',
            'tax_code': settings.TAX_CODE_FOOD,
            'amount': 10000
        }

        response = self.client.post(
            reverse('tax:tax-items'),
            data=data,
            format='json'
        )
        response_data = response.data

        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data)
        self.assertEqual(response_data['name'], 'food 1')
        self.assertEqual(response_data['tax_code'], settings.TAX_CODE_FOOD)
        self.assertEqual(Decimal(response_data['amount']), 10000)

    def test_create_new_tax_item_with_invalid_tax_code(self):
        data = {
            'name': 'food 1',
            'tax_code': 100,
            'amount': 10000
        }

        response = self.client.post(
            reverse('tax:tax-items'),
            data=data,
            format='json'
        )
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_tax_item_list(self):
        # Make dummy tax item
        mommy.make(TaxItem)

        response = self.client.get(reverse('tax:tax-items'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
