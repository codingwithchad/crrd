from django.contrib import admin

from .models import UseCat, ReuseItem, Business, RepCat, RepairItem, RepBusiness


#Allows 4 text boxes to be displayed by default while adding items in Use Cat
#more can be inserted within the browser
class ReuseItemInline(admin.TabularInline):
	model = ReuseItem
	extra = 4
#This allows the UseCat for the admin page
#Category Name is on top and 4 text boxes for Item names are underneath
#more text boxes can be added on the fly
class UseCatAdmin(admin.ModelAdmin):
	fieldset = [
	(None, {'fields': ['catName']}),
	('Date information', {'fields':['lastUpdate']}),
	]
	inlines = [ReuseItemInline]
	list_display = ('catName', 'lastUpdate')
	
class RepairItemInline(admin.TabularInline):
	model = RepairItem
	extra = 4

class RepCatAdmin(admin.ModelAdmin):
	fieldset = [
	(None, {'fields': ['repName']}),
	('Date information', {'fields':['lastUpdate']}),
	]
	inlines = [RepairItemInline]
	list_display = ('repName', 'lastUpdate')

#trying to pretty up the items-business relationship for the admin page
class busItemInline(admin.TabularInline):
	model = Business.items.through

class busItemAdmin(admin.ModelAdmin):
	inlines = [busItemInline,]
class busAdmin(admin.ModelAdmin):
	inlines = [busItemInline,] 
	exclude = ('items',)

#trying to pretty up the items-business relationship for the admin page
class repBusItemInline(admin.TabularInline):
	model = RepBusiness.repairItem.through

class RepBusItemAdmin(admin.ModelAdmin):
	inlines = [repBusItemInline,]
class RepBusAdmin(admin.ModelAdmin):
	inlines = [repBusItemInline,] 
	exclude = ('repairItem',)



	
# Register your models here.

admin.site.register(UseCat, UseCatAdmin)
admin.site.register(ReuseItem)
admin.site.register(RepCat, RepCatAdmin)
admin.site.register(RepairItem)
admin.site.register(Business, busAdmin)
admin.site.register(RepBusiness, RepBusAdmin)


