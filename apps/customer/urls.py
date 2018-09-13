from django.conf.urls import url

from .views import (
    Login,
    GetBills,
    GetBillDetail
)

app_name = 'user'

urlpatterns = [
    url(r'^login/?$', Login.as_view(), name='user-login'),
    url(r'^bills/?$', GetBills.as_view(), name='get-user-bills'),
    url(r'^bill/detail/(?P<bill_id>[\d]+)/?$', GetBillDetail.as_view(),
        name='get-user-bill-detail'),
]
