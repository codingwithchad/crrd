import datetime
from django.db import models
from django.utils import timezone

class ReuseCategories(models.Model):
    name = models.CharField(max_length=255)
    lastUpdate = models.DateTimeField('date updated')
    def __unicode__(self):
        return self.name

class ReuseItem(models.Model):
    itemCategory = models.ForeignKey(ReuseCategories)
    itemName = models.CharField(max_length=255)
    lastUpdate = models.DateTimeField('last updated')
    def __unicode__(self):
        return self.itemName



