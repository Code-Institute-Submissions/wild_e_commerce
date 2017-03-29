from __future__ import unicode_literals

from django.db import models
from products.models import Product

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True)
    #products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

# Create your models here.
class SubCategory1(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Category, null=True)

    #products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class SubCategory2(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(SubCategory1, null=True)

    #products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name

class SubCategory3(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(SubCategory2, null=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name





