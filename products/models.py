from __future__ import unicode_literals

from django.db import models

#from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name


class Status(models.Model):
    status = models.CharField(max_length=254, default='')
    product = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return self.status



class NewProducts (models.Model):
    status = models.ForeignKey(Status, null=True)
    name = models.ForeignKey(Product, null=True)
    description = models.TextField(Product, null=True)
    price = models.DecimalField(Product,max_digits=6, decimal_places=2, null=True)
    image =  models.ImageField(Product, null=True)
    brand = models.CharField(Product,max_length=100, null=True)

    def __str__(self):
        return self.name
