from __future__ import unicode_literals

from django.db import models





class Status(models.Model):
    name = models.CharField(max_length=254, default='')


    def __str__(self):
        return self.name
