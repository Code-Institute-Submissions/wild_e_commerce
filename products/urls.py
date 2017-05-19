from django.conf.urls import url
from .views import get_productsdetails, products
from accounts.views import login


urlpatterns = \
    [
        url(r'^$', products, name='products'),
        url(r'^(?P<id>\d+)/$', get_productsdetails, name='product_details'),
        url(r'^products/(?P<id>\d+)$', login, name='login'),
    ]
