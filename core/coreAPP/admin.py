from django.contrib import admin
from .models import UseCat, UseItem, BusItem, Business, RepCat, RepItem, BusRepItem
from django.contrib.contenttypes.admin import GenericTabularInline

#Allows 4 text boxes to be displayed by default while adding items in Use Cat
#more can be inserted within the browser
class UseItemInline(admin.TabularInline):
	model = UseItem
	extra = 4
#This allows the UseCat for the admin page
#Category Name is on top and 4 text boxes for Item names are underneath
#more text boxes can be added on the fly
class UseCatAdmin(admin.ModelAdmin):
	fieldset = [
	(None, {'fields': ['catName']}),
	('Date information', {'fields':['lastUpdate']}),
	]
	inlines = [UseItemInline]
	list_display = ('catName', 'lastUpdate')
	
class RepItemInline(admin.TabularInline):
	model = RepItem
	extra = 4

class RepCatAdmin(admin.ModelAdmin):
	fieldset = [
	(None, {'fields': ['repName']}),
	('Date information', {'fields':['lastUpdate']}),
	]
	inlines = [RepItemInline]
	list_display = ('repName', 'lastUpdate')


	
# Register your models here.
admin.site.register(UseCat, UseCatAdmin)
admin.site.register(UseItem)
admin.site.register(RepCat, RepCatAdmin)
admin.site.register(RepItem)
admin.site.register(BusItem)
admin.site.register(Business)

