from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.shortcuts import render
from .models import Brand


def root_brands(request):
    brands = Brand.objects.order_by('name')
    args = { 'brands': brands, 'products': {}}
    return render(request, 'brands.html', args)

def get_brands(request, id):
    this_brand = get_object_or_404(Brand, pk=id)
    products = Product.objects.filter(brandname_id=this_brand)
    args = { 'brand': this_brand,'products': products}
    return render(request, 'branddetails.html', args)

