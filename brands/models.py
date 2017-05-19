from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images', null=True, blank=True )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name



