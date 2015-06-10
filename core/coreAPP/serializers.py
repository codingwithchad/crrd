from django.forms import widgets
from rest_framework  import serializers
from .models import UseCat, ReuseItem, BusItem, Business, RepCat, RepairItem, BusinessRepairItem
from django.http import httpResponse

data = serializers.serialize("json", UseCat.all())
response = httpResponse()
response.write("hello world")