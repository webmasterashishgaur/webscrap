"""HELLO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.site_header = "MyChoize Admin"
admin.site.index_title = "Welcome to MyChoize "
admin.site.site_title = "MyChoize"

admin.site.unregister(User)

# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    
   ]
