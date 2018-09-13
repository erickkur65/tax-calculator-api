from django.conf.urls import url

from .views import CreateBill

app_name = 'bill'

urlpatterns = [
    url(r'^$', CreateBill.as_view(), name='create-bill'),
]
