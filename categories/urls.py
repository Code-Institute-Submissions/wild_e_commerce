from django.conf.urls import url
from .views import root_categories, get_category
from products.views import get_productsdetails



urlpatterns = [
   url(r'^$', root_categories, name='categories'),
   url(r'^(?P<id>\d+)$', get_category, name='category'),
   url(r'^products/(?P<id>\d+)$', get_productsdetails, name='product_details'),

    ]