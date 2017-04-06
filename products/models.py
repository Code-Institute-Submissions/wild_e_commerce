from __future__ import unicode_literals

from django.db import models
from brands.models import Brand
#from categories.models import Category



class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    brand = models.ForeignKey(Brand, null=True)


    def __str__(self):
        return self.name


