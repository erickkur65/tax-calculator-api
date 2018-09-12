from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url(r'^tax/', include('tax.urls'), name='tax'),
]
