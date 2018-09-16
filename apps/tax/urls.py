from django.conf.urls import url

from .views import TaxItemView

app_name = 'tax'

urlpatterns = [
    url(r'^items/?$', TaxItemView.as_view(), name='tax-items')
]
