"""TFAProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from hello.views import map, sightings, update_sighting, squirrel_data_create, display_r, home

'''
Mapping URLs to the respective Views function and the HTML template
'''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', map),
    re_path(r'sightings/add',squirrel_data_create),
    path('sightings/<str:unique_squirrel_id>', update_sighting),
    path('sightings/', sightings),
    path('display',display_r),
    path('',home),
    ]