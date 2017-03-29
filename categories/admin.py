from django.contrib import admin
from .models import Category, SubCategory1, SubCategory2, SubCategory3

# Register your models here.
admin.site.register(Category)

admin.site.register(SubCategory1)
admin.site.register(SubCategory2)
admin.site.register(SubCategory3)

