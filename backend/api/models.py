from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

class ChurchEvent(models.Model):
    title = models.CharField(max_length=1000, blank=False)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    description = models.CharField(max_length=1000, blank=False)
    address = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return str(self.title)


class Alert(models.Model):
    text = models.CharField(max_length=1000, blank=False)
    startdate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return str(self.text)

class Image(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    image = models.CharField(max_length=1000,blank=False)

    def __str__(self):
        return str(self.name)

