from django.shortcuts import render, get_object_or_404
from models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.template.context_processors import csrf


def get_index(request):
    return render(request, "index.html")


# Create your views here.
def products(request):
    products_all = Product.objects.all()
    args = {}
    args.update(csrf(request))
    return render(request, 'products.html', {'products':products_all}, args)


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Create your views here.
def get_productsdetails(request, id):
    product = get_object_or_404(Product, pk=id)
    product.save()
    return render(request, "productdetails.html", {'product': product})


def new_products(request):
    statnew = Product.objects.filter(statusname_id=1)
    return {'new_products': statnew}


def special_products(request):
    statspecial = Product.objects.filter(statusname_id=2)
    return {'special_products': statspecial}


def featured_products(request):
    statfeatured = Product.objects.filter(statusname_id=3)
    return {'featured_products': statfeatured}


def all_products(request):
    stat = Product.objects.all()
    return {'all_products': stat}
