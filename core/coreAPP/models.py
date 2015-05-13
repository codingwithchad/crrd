import datetime
from django.db import models
from django.utils import timezone


#class Admin(models.Model):
#    userName = models.CharField(max_length=200)
#    password = models.CharField(max_length=200)
#    permissions = models.CharField(max_length=200)
#    def __str__(self):
#        return self.userName

class UseCat(models.Model):
    catName = models.CharField(max_length=200)
#    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('date updated', blank=True)
    def __str__(self):
        return self.catName

class UseItems(models.Model):
    itemCat = models.ForeignKey(UseCat)
    itemName = models.CharField(max_length=200)
#    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('last updated', blank=True)
    def __str__(self):
        return self.itemName

class BusItem(models.Model):
    businesses = models.ForeignKey('coreAPP.Business')
    items = models.ForeignKey(UseItems)

class Business(models.Model):
    busName = models.CharField(max_length=200)
    repairBus = models.NullBooleanField()
    address1 = models.CharField(max_length=200, blank=True)
    address2 =  models.CharField(max_length=200, blank=True)
    city =  models.CharField(max_length=200, blank=True)
    state =  models.CharField(max_length=200, blank=True)
    zipcode =  models.IntegerField(blank=True, null=True)
    phone1 =  models.CharField(max_length=200, blank=True)
    phone2 =  models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    web =  models.URLField(max_length=200, blank=True)
    geolocal =  models.CharField(max_length=200, blank=True)
    hours =  models.CharField(max_length=200, blank=True)
#    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('last updated', blank=True, null=True)
    def __str__(self):
        return self.busName

class RepCat(models.Model):
    repName = models.CharField(max_length=200)
#    adminID = models.ForeignKey(Admin)
    def __str__(self):
        return self.repName






