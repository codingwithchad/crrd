from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
from django.core import serializers
from .models import UseCat, ReuseItem, BusItem, Business, RepCat, RepairItem, BusinessRepairItem

def index(request):
    now = datetime.datetime.now()
    html = "<html><body> the time is %s.</body></html>" % now
    return HttpResponse(html)

def viewUseCat(request):
    data = serializers.serialize('json', UseCat.objects.all(), fields =('id', 'catName'))
   
    return HttpResponse(data)

def viewUseItems(request, catID):
    #showItems = ReuseItem.objects.filter(itemCat_id=catID)
    response = serializers.serialize('json', ReuseItem.objects.filter(itemCat_id=catID), fields =('id', 'itemName'))
   
    return HttpResponse(response)

def viewBusiness(request, itemID):
    thisBus = BusItem.objects.filter(items_id=itemID)
    for x in thisBus:
        response = serializers.serialize('json', Business.objects.filter(id=x.id))

   
    #response = serializers.serialize('json', BusItem.objects.filter(items_id=itemID), fields =('business_id'))

    return HttpResponse(response)

# Create your views here.
