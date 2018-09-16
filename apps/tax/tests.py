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
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)

    def test_get_tax_item_list(self):
        mommy.make(TaxItem)

        response = self.client.get(reverse('tax:tax-items'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
