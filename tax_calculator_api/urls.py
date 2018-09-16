from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^tax/', include('tax.urls'), name='tax'),
    url(r'^transaction/', include('transaction.urls'), name='transaction'),
    url(r'^user/', include('user.urls'), name='user'),
]
