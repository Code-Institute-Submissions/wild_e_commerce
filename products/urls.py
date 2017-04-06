from django.conf.urls import url
from .views import products,get_productsdetails



urlpatterns = [
    url(r'^$', products, name='products'),
    url(r'^(?P<id>\d+)/$', get_productsdetails, name='product_details'),

]