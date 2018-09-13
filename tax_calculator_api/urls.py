from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^bill/', include('bill.urls'), name='bill'),
    url(r'^tax/', include('tax.urls'), name='tax'),
    url(r'^user/', include('user.urls'), name='user'),
]
