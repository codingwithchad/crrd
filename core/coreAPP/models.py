import datetime
from django.db import models
from django.utils import timezone

class UseCat(models.Model):
    catName = models.CharField('Category Name', max_length=200, unique=True)
    lastUpdate = models.DateTimeField('date updated', auto_now=True, blank=True)
    def __str__(self):
        return self.catName
    class Meta:
        verbose_name = "Reuse Category"
        verbose_name_plural = "Reuse Categories"
        
class ReuseItem(models.Model):
    itemCat = models.ForeignKey(UseCat)
    itemName = models.CharField('item name', max_length=200, unique=True)
    lastUpdate = models.DateTimeField('last updated', auto_now=True, blank=True)
    def __str__(self):
        return self.itemName
    class Meta:
        verbose_name = "Reuse Item"
        verbose_name_plural = "Reuse Items"    

class Business(models.Model):
    #items = models.ForeignKey(ReuseItem)
    items = models.ManyToManyField(ReuseItem, blank=True)
    busName = models.CharField('Business Name', max_length=200, unique=True)
    address1 = models.CharField('Address', max_length=200, blank=True)
    address2 =  models.CharField('Address', max_length=200, blank=True)
    city =  models.CharField(max_length=200, blank=True)
    state =  models.CharField(max_length=200, blank=True)
    zipcode =  models.IntegerField(blank=True, null=True)
    phone1 =  models.CharField(max_length=200, blank=True)
    phone2 =  models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    web =  models.URLField(max_length=200, blank=True)
    longitude =  models.CharField(max_length=200, blank=True)
    latitude =  models.CharField(max_length=200, blank=True)
    hours =  models.CharField(max_length=200, blank=True)
    lastUpdate = models.DateTimeField('last updated', auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.busName

class RepCat(models.Model):
    repName = models.CharField(max_length=200, unique=True)
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

class RepBusiness(models.Model):
    repairItem = models.ManyToManyField(RepairItem, blank=True)
    busName = models.CharField('Business Name', max_length=200, unique=True)
    address1 = models.CharField('Address', max_length=200, blank=True)
    address2 =  models.CharField('Address', max_length=200, blank=True)
    city =  models.CharField(max_length=200, blank=True)
    state =  models.CharField(max_length=200, blank=True)
    zipcode =  models.IntegerField(blank=True, null=True)
    phone1 =  models.CharField(max_length=200, blank=True)
    phone2 =  models.CharField(max_length=200, blank=True)
    email = models.EmailField(blank=True)
    web =  models.URLField(max_length=200, blank=True)
    longitude =  models.CharField(max_length=200, blank=True)
    latitude =  models.CharField(max_length=200, blank=True)
    hours =  models.CharField(max_length=200, blank=True)
    lastUpdate = models.DateTimeField('last updated', auto_now=True, blank=True, null=True)
    def __str__(self):
        return self.busName
