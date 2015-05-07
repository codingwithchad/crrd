import datetime
from django.db import models
from django.utils import timezone


class Admin(models.Model):
    userName = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    permissions = models.CharField(max_length=200)
    def __str__(self):
        return self.userName

class UseCat(models.Model):
    catName = models.CharField(max_length=200)
    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('date updated')
    def __str__(self):
        return self.catName

class UseItems(models.Model):
    itemCat = models.ForeignKey(UseCat)
    itemName = models.CharField(max_length=200)
    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('last updated')
    def __str__(self):
        return self.itemName

class BusItem(models.Model):
    businesses = models.ForeignKey('coreAPP.Business')
    items = models.ForeignKey(UseItems)

class Business(models.Model):
    busName = models.CharField(max_length=200)
    repairBus = models.NullBooleanField()
    address1 = models.CharField(max_length=200)
    address2 =  models.CharField(max_length=200, blank=True, null=True)
    city =  models.CharField(max_length=200)
    state =  models.CharField(max_length=200)
    zipcode =  models.IntegerField()
    phone1 =  models.CharField(max_length=200)
    phone2 =  models.CharField(max_length=200)
    email = models.EmailField()
    web =  models.URLField(max_length=200)
    geolocal =  models.CharField(max_length=200)
    hours =  models.CharField(max_length=200)
    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('last updated')
    def __str__(self):
        return self.busName

class RepCat(models.Model):
    repName = models.CharField(max_length=200)
    adminID = models.ForeignKey(Admin)
    def __str__(self):
        return self.repName






