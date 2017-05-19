"""wild_e_commerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from index.views import get_index

from products import urls as products_urls
from categories import urls as categories_urls
from accounts import urls as accounts_urls
from cart import urls as cart_urls
from payments import urls as payments_urls
from brands import urls as brands_urls

from rest_framework import routers
from products import views as product_views
from cart import views as cart_views
from wild_e_commerce.views import about_us, contact_us


router = routers.DefaultRouter()
router.register(r'products', product_views.ProductViewSet)
router.register(r'users', cart_views.UserViewSet)
router.register(r'cart', cart_views.CartItemViewSet)


urlpatterns = \
    [
        url(r'^api/', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^admin/', admin.site.urls),
        url(r'^$', get_index),
        url(r'^categories/', include(categories_urls)),
        url(r'^products/', include(products_urls)),
        url(r'^cart/', include(cart_urls)),
        url(r'^accounts/', include(accounts_urls)),
        url(r'^payments/', include(payments_urls)),
        url(r'^$', get_index, name='index'),
        url(r'user/', include(accounts_urls)),
        url(r'^brands/', include(brands_urls)),
        url(r'^aboutus/', about_us, name='aboutus'),
        url(r'^contactus/', contact_us, name='contactus'),
        url(r'^login/', include(accounts_urls)),
    ]
