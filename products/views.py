from django.shortcuts import render, get_object_or_404
from models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.template.context_processors import csrf
from categories.models import Category
from brands.models import Brand

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
    #product.views += 1
    product.save()
    return render(request, "productdetails.html", {'product': product})


def get_productslist(request, id):
    product_list = get_object_or_404(Product, pk=id)
    products = product_list.products.all()
    return render(request, "productslist.html", {'product': products})

