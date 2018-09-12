from django.conf.urls import url

from .views import CreateTax

app_name = 'tax'

urlpatterns = [
    url(r'^$', CreateTax.as_view(), name='create-tax')
]
