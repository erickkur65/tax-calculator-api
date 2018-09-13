from django.conf.urls import url

from .views import CreateTaxItem

app_name = 'tax'

urlpatterns = [
    url(r'^items/?$', CreateTaxItem.as_view(), name='create-tax-item'),
]
