from django.conf.urls import url

from .views import (
    UserBill,
    UserBillDetail
)

app_name = 'transaction'

urlpatterns = [
    url(r'^bills/?$', UserBill.as_view(), name='user-bills'),
    url(r'^bill/(?P<bill_id>[\d]+)/?$', UserBillDetail.as_view(),
        name='user-bill-detail'),
]
