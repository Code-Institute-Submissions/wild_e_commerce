from django.conf.urls import url
from .views import  root_brands, get_brands

urlpatterns = [
    url(r'^$', root_brands, name='brands'),
    url(r'^(?P<id>\d+)$', get_brands, name='brand'),

    ]

