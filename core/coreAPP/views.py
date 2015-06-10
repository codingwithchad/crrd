from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import UseCat, ReuseItem, BusItem, Business, RepCat, RepairItem, BusinessRepairItem

def index(request):
    now = datetime.datetime.now()
    html = "<html><body> the time is %s.</body></html>" % now
    return HttpResponse(html)

def viewUseCat(request):
    allCategories = UseCat.objects.all()
    output = ','.join([str(x.id) for x in allCategories])
    return HttpResponse(output)

def viewUseItems(request, catID):
    showItems = ReuseItem.objects.order_by('itemName')
    response = ""
    for x in showItems:
        
        #return HttpResponse("Double Winner")
        response = ','.join("X")
        response = ','.join([x.itemName])
        response = ','.join([catID])
        response = ','.join([x.itemCat])
    #response = "List all the items whos parent is %s " % catID
    return HttpResponse(response)

def viewBusiness(request, itemID):
    return HttpResponse("list all business that accept items in  %s" % itemID)

# Create your views here.
