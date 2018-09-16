from django.conf.urls import url

from .views import (
    CreateBill,
    GetUserBills,
    GetUserBillDetail
)

app_name = 'bill'

urlpatterns = [
    url(r'^$', CreateBill.as_view(), name='create-bill'),
    url(r'^bills/?$', GetUserBills.as_view(), name='get-user-bills'),
    url(r'^bill/detail/(?P<bill_id>[\d]+)/?$', GetUserBillDetail.as_view(),
        name='get-user-bill-detail'),
]
