from django.conf.urls import url
from .views import console


urlpatterns = [
    url(r'^$',console),
]