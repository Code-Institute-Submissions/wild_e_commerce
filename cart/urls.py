from django.conf.urls import url
from .views import user_cart, add_to_cart, remove_from_cart
#from django.views import static
#from wild_e_commerce.settings import STATIC_ROOT

urlpatterns = [
    url(r'^$', user_cart, name='cart'),
    url(r'^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url(r'^remove/(?P<id>\d+)', remove_from_cart, name='remove_from_cart'),
    #url(r'^static/(?P<path>.*)$', static.serve,{'document_root': STATIC_ROOT}),


]