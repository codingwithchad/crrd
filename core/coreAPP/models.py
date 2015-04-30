import datetime
from django.db import models
import django.utils import timezone

class ReuseCategories(models.Model):
    name = models.CharField(max_length=255)
    lastUpdate = models.DateTimeField('date updated')
    def __str__(self):
        return sel.ReuseCategories

class ReuseItem(models.Model):
    itemCategory = models.ForeignKey(ReuseCategories)
    itemName = models.CharField(max_length=255)
    lastUpdate = models.DateTimeField('last updated')
    def __str__(self):
        return self.ReuseItem



