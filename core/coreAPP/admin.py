from django.contrib import admin
from .models import UseCat, UseItems

class UseCatAdmin(admin.ModelAdmin):
	fieldset = [
	(None, {'fields': ['catName']}),
	('Date information', {'fields':['lastUpdate']}),
	]

# Register your models here.
admin.site.register(UseCat, UseCatAdmin)
admin.site.register(UseItems)

