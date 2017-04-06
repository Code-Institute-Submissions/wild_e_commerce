from django.shortcuts import render
from categories.models import Category


# Create your views here.

def get_index(request):
    categories = Category.objects.filter(parent=None)
    args = {'categories': categories}
    return render(request ,"index.html", args)

