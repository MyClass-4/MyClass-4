# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from MyClass import settings

urlpatterns = [
    url(r'^login$', 'User.views.login', name = 'login'),
    url(r'^logout$', 'User.views.logout', name = 'logout'),
    url(r'^change_avatar$', 'User.views.change_avatar', name="change_avatar"),
    # url(r'^$', 'User.views.index', name = 'index'),
]
