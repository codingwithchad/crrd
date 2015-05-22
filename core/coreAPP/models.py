import datetime
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey


#class Admin(models.Model):
#    userName = models.CharField(max_length=200)
#    password = models.CharField(max_length=200)
#    permissions = models.CharField(max_length=200)
#    def __str__(self):
#        return self.userName

class UseCat(models.Model):
    catName = models.CharField('Category Name', max_length=200, unique=True)
#    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('date updated', auto_now=True, blank=True)
    def __str__(self):
        return self.catName

class UseItem(models.Model):
    itemCat = models.ForeignKey(UseCat)
    itemName = models.CharField('item name', max_length=200, unique=True)
#    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('last updated', auto_now=True, blank=True)
    def __str__(self):
        return self.itemName



class Business(models.Model):
    busName = models.CharField('Business Name', max_length=200, unique=True)
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
    lastUpdate = models.DateTimeField('last updated', auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.busName



class BusItem(models.Model):
    businesses = models.ForeignKey(Business)
    items = models.ForeignKey(UseItem)
    busItemObject = GenericForeignKey("content_type", "object_id")
    lastUpdate = models.DateTimeField('last updated', auto_now=True, blank=True)
    def __str__(self):
        return self.businesses.busName + "-" + self.items.itemName

class RepCat(models.Model):
    repName = models.CharField(max_length=200, unique=True)
#    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('last update', auto_now=True, blank=True)
    def __str__(self):
        return self.repName

class RepItem(models.Model):
    RepCat = models.ForeignKey(RepCat)
    RepItemName = models.CharField(max_length=200, unique=True)
    lastUpdate = models.DateTimeField('last update', auto_now=True, blank=True)
    def __str__(self):
        return self.RepItemName

class BusRepItem(models.Model):
    business = models.ForeignKey('coreAPP.Business')
    repItem = models.ForeignKey(RepItem)
    lastUpdate = models.DateTimeField('last update', auto_now=True, blank=True)
    def __str__(self):
        return self.business.busName +"-"+ self.repItem.RepItemName






