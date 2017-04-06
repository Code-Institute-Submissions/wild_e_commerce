from django.shortcuts import render, get_object_or_404
from .models import Category
from products.models import Product
from django.shortcuts import render
# Create your views here.
def root_categories(request):
    categories = Category.objects.filter(parent=None)

    args = { 'categories': categories, 'subcategories': {}, 'products': {}}
    return render(request, 'categories.html', args)


def get_category(request, id):
    categories = Category.objects.filter(parent=None)

    parent = get_object_or_404(Category, pk=id)
    subcategories = Category.objects.filter(parent=parent)

    products = parent.products.all()

    args = {'categories': categories, 'subcategories': subcategories, 'products': products}

    return render(request, 'categories.html', args)


# Create your views here.
def get_productsdetails(request, id):
    parent = get_object_or_404(Product, pk=id)
    categories = Category.objects.filter(parent=None)
    products = parent.objects.all()
    subcategories = Category.objects.filter(parent=parent)
    args = {'categories': categories, 'subcategories': subcategories, 'products': products}
    return render(request, 'productdetails.html', {'productinfo':products}, args)

#########################


#def get_cat(request):
#    return render(request ,"categories.html")
