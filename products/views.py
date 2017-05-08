from django.shortcuts import render, get_object_or_404
from models import Product, Status
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.template.context_processors import csrf
from categories.models import Category
from brands.models import Brand

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



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
    statnew = Product.objects.filter(statusname_id=4)
    return {'new_products': statnew}

def special_products(request):
    statspecial = Product.objects.filter(statusname_id=5)
    return {'special_products': statspecial}

def featured_products(request):
    statfeatured = Product.objects.filter(statusname_id=6)
    return {'featured_products': statfeatured}

def all_products(request):
    stat = Product.objects.all()
    return {'all_products': stat}


#def product_listing(request):
 #   product_list = Product.objects.all()
 #   paginator = Paginator(product_list, 4) # Show 25 contacts per page

  #  page = request.GET.get('page')
  #  try:
  #      productx = paginator.page(page)
  #  except PageNotAnInteger:
        # If page is not an integer, deliver first page.
  #      productx = paginator.page(1)
   # except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
    #    productx = paginator.page(paginator.num_pages)

   # return render(request, 'newcategoryproducts.html', {'product_list': productx})