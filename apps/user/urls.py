from django.conf.urls import url

from .views import (
    Login,
    Register
)

app_name = 'user'

urlpatterns = [
    url(r'^login/?$', Login.as_view(), name='user-login'),
    url(r'^register/?$', Register.as_view(), name='user-register'),
]
