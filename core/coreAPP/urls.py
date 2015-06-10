from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^usecat/$', views.viewUseCat, name='categories'),
    
    url(r'^(?P<catID>[A-Za-z]+)/useitems/$', views.viewUseItems, name='items'),
    url(r'^(?P<itemID>[0-9]+)/business/$', views.viewBusiness, name='business'),
    ]