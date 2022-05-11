from http import server
from xml.etree.ElementInclude import include
from django.urls import path
from home.views import web
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path("web", views.web, name='web'),
    path("login", views.login_user, name='login'),
    path("scrapzoom", views.scrapzoom, name='scrapzoom'),
    path("scraprevv", views.scraprevv, name='scraprevv'),
    path("logout", views.pagelogout, name='logout'),
    path("waste",views.waste_file,name='waste'),
    
    
    

]

