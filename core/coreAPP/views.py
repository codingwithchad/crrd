from django.shortcuts import render
from django.http import HttpResponse
import datetime
import json
from django.core import serializers
from .models import UseCat, ReuseItem, Business, RepCat, RepairItem, RepBusiness
def index(request):
    now = datetime.datetime.now()
    html = "<html><body> the time is %s.</body></html>" % now
    return HttpResponse(html)

def viewUseCat(request):
    response = serializers.serialize('json', UseCat.objects.all(), fields =('id', 'catName'))
    return HttpResponse(response)

def viewUseItems(request, catID):
    response = serializers.serialize('json', ReuseItem.objects.filter(itemCat_id=catID), fields =('id', 'itemName'))
    return HttpResponse(response)

def viewBusiness(request, itemID):
    response = serializers.serialize('json', Business.objects.filter(items=itemID), fields=('id', 'busName'))
    return HttpResponse(response)

def viewBusDetail(request, busID):
    response = serializers.serialize('json', Business.objects.filter(id=busID))
    return HttpResponse(response)

def viewRepCat(request):
    repRes = serializers.serialize('json', RepCat.objects.all(), fields =('id', 'repName'))
    return HttpResponse(repRes)

def viewRepItems(request, repCatID):
    response = serializers.serialize('json', RepairItem.objects.filter(RepCat_id=repCatID), fields =('id', 'RepItemName'))
    return HttpResponse(response)

def viewRepairBusiness(request, repItemID):
    response = serializers.serialize('json', RepBusiness.objects.filter(repairItem=repItemID), fields=('id', 'busName'))
    return HttpResponse(response)

def viewRepBusDetail(request, repBusID):
    response = serializers.serialize('json', RepBusiness.objects.filter(id=repBusID))
    return HttpResponse(response)
