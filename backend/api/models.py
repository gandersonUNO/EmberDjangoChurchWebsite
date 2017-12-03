from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

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

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')
