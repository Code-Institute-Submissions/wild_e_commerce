from django.shortcuts import render
from models import Product
#from rest_framework import viewsets
#from .serializers import ProductSerializer
from django.template.context_processors import csrf


def get_index(request):
    return render(request, "index.html")

# Create your views here.
def products(request):
    products_all = Product.objects.all()
    return render(request, 'products.html', {'products':products_all})