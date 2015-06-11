from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    
    url(r'^usecat/$', views.viewUseCat, name='categories'),
    url(r'^(?P<catID>[0-9]+)/useitems/$', views.viewUseItems, name='items'),
    url(r'^(?P<itemID>[0-9]+)/business/$', views.viewBusiness, name='businesses'),

    url(r'^repcat/repair/$', views.viewRepCat, name='repair categories'),
    url(r'^(?P<repCatID>[0-9]+)/repitems/$', views.viewRepItems, name='repair items'),
    url(r'^(?P<repItemID>[0-9]+)/repbusiness/$', views.viewRepairBusiness, name='repair businesses'),

    ]