from django.shortcuts import render, get_object_or_404
from .models import Category
from products.models import Product
from django.shortcuts import render


# Create your views here.
def root_categories(request):
    categories = Category.objects.filter(parent=None)

    args = {'categories': categories, 'subcategories': {}, 'products': {}}
    return render(request, 'categories.html', args)


def root_categories_context(request):
    categories = Category.objects.filter(parent=None)
    return {'root_categories': categories}


def get_category(request, id):
    this_category = get_object_or_404(Category, pk=id)

    crumbs = []

    crumb = this_category
    while crumb != None:
        crumbs.insert(0, crumb)
        crumb = crumb.parent

    subcategories = Category.objects.filter(parent=this_category)

    products = this_category.products.all()

    args = {'categories': subcategories, 'products': products, 'crumbs': crumbs}
    return render(request, 'categories.html', args)


def get_productsdetails(request, id):
    parent = get_object_or_404(Product, pk=id)
    categories = Category.objects.filter(parent=None)
    products = parent.objects.all()
    subcategories = Category.objects.filter(parent=parent)
    args = {'categories': categories, 'subcategories': subcategories, 'products': products}
    return render(request, 'productdetails.html', {'productinfo': products}, args)

