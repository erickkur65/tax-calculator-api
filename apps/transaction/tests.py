from decimal import Decimal

from model_mommy import mommy
from rest_framework import status
from rest_framework.reverse import reverse

from tax import settings as tax_settings
from tax.models import TaxItem
from transaction.models import Bill
from user.models import User
from utils.test import CustomerTestCase


class BillTest(CustomerTestCase):
    email = 'test@gmail.com'
    password = 'test123'

    def test_create_new_user_bill(self):
        tax_item_1 = mommy.make(
            TaxItem,
            tax_code=tax_settings.TAX_CODE_FOOD,
            amount=10000
        )
        tax_item_2 = mommy.make(
            TaxItem,
            tax_code=tax_settings.TAX_CODE_FOOD,
            amount=20000
        )

        data = {
            'tax_items': [
                {
                    'tax_item_id': tax_item_1.id,
                    'tax_code': tax_item_1.tax_code,
                    'amount': tax_item_1.amount,
                    'qty': 2
                },
                {
                    'tax_item_id': tax_item_2.id,
                    'tax_code': tax_item_2.tax_code,
                    'amount': tax_item_2.amount,
                    'qty': 1
                }
            ]
        }

        response = self.client.post(
            reverse('transaction:user-bills'),
            data=data,
            format='json'
        )
        response_data = response.data

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data)
        self.assertEqual(Decimal(response_data['sub_total']), 40000)
        self.assertEqual(Decimal(response_data['tax_total']), 4000)
        self.assertEqual(Decimal(response_data['grand_total']), 44000)

    def test_create_new_user_bill_with_invalid_tax_item(self):
        tax_item_1 = mommy.make(
            TaxItem,
            tax_code=tax_settings.TAX_CODE_FOOD,
            amount=10000
        )

        data = {
            'tax_items': [
                {
                    'tax_item_id': 100,
                    'tax_code': tax_item_1.tax_code,
                    'amount': tax_item_1.amount,
                    'qty': 2
                }
            ]
        }

        response = self.client.post(
            reverse('transaction:user-bills'),
            data=data,
            format='json'
        )

        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_user_bill_list(self):
        user_login = User.objects.get(email=self.email)
        dummy_user = mommy.make(User)

        # Make dummy bill list
        mommy.make(Bill, user_id=user_login.id)
        mommy.make(Bill, user_id=dummy_user.id)

        response = self.client.get(reverse('transaction:user-bills'))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 1)


class BillDetailTest(CustomerTestCase):
    email = 'test@gmail.com'
    password = 'test123'

    def test_get_user_bill_detail(self):
        user_login = User.objects.get(email=self.email)
        dummy_user = mommy.make(User)

        # Make dummy bill list
        bill_1 = mommy.make(Bill, user_id=user_login.id)
        bill_2 = mommy.make(Bill, user_id=dummy_user.id)

        response = self.client.get(
            reverse('transaction:user-bill-detail', args=[bill_1.id]))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_user_bill_detail_with_invalid_bill_id(self):
        user_login = User.objects.get(email=self.email)
        dummy_user = mommy.make(User)

        # Make dummy bill list
        bill_1 = mommy.make(Bill, user_id=user_login.id)
        bill_2 = mommy.make(Bill, user_id=dummy_user.id)

        response = self.client.get(
            reverse('transaction:user-bill-detail', args=[bill_2.id]))
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
