# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from MyClass import settings

urlpatterns = [
	url(r'^coding$', 'CodeLib.views.coding', name = 'coding'),
]
