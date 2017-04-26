from django.conf.urls import url
from .views import get_productsdetails, products#, get_productslist



urlpatterns = [
    url(r'^$', products, name='products'),
    url(r'^(?P<id>\d+)/$', get_productsdetails, name='product_details'),
    #url(r'^productslist/(?P<id>\d+)$', get_productslist, name='product_list'),
]