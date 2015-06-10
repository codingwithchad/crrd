import datetime
from django.db import models
from django.utils import timezone
#from django.contrib.contenttypes.fields import GenericForeignKey
#from django.contrib.contenttypes.models import ContentType


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
    class Meta:
        verbose_name = "Reuse Category"
        verbose_name_plural = "Reuse Categories"
        
class ReuseItem(models.Model):
    itemCat = models.ForeignKey(UseCat)
    itemName = models.CharField('item name', max_length=200, unique=True)
#   adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('last updated', auto_now=True, blank=True)
    def __str__(self):
        return self.itemName
    class Meta:
        verbose_name = "Reuse Item"
        verbose_name_plural = "Reuse Items"    



class Business(models.Model):
    busName = models.CharField('Business Name', max_length=200, unique=True)
    repairBus = models.NullBooleanField()
    address1 = models.CharField('Address', max_length=200, blank=True)
    address2 =  models.CharField('Address', max_length=200, blank=True)
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
    items = models.ForeignKey(ReuseItem)
    lastUpdate = models.DateTimeField('last updated', auto_now=True, blank=True)
    def __str__(self):
        return self.businesses.busName + "-" + self.items.itemName
    class Meta:
        verbose_name = "Reuse Business Item"
        verbose_name_plural = "Reuse Business Items"

class RepCat(models.Model):
    repName = models.CharField(max_length=200, unique=True)
#    adminID = models.ForeignKey(Admin)
    lastUpdate = models.DateTimeField('last update', auto_now=True, blank=True)
    def __str__(self):
        return self.repName
    class Meta:
        verbose_name = "Repair Category"
        verbose_name_plural = "Repair Categories"

class RepairItem(models.Model):
    RepCat = models.ForeignKey(RepCat)
    RepItemName = models.CharField(max_length=200, unique=True)
    lastUpdate = models.DateTimeField('last update', auto_now=True, blank=True)
    def __str__(self):
        return self.RepItemName
    class Meta:
        verbose_name = "Repair Item"
        verbose_name_plural = "Repair Items"

class BusinessRepairItem(models.Model):
    business = models.ForeignKey(Business)
    repairItem = models.ForeignKey(RepairItem)
    def __str__(self):
        return self.business.busName +"-"+ self.repairItem.RepItemName
    class Meta:
        verbose_name = "Repair Business Item"
        verbose_name_plural = "Repair Business Items"






