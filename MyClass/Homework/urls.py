# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from MyClass import settings

urlpatterns = [
    url(r'^upload_homework$', 'Homework.views.upload_homework', name = 'upload_homework'),
    url(r'^statistic$', 'Homework.views.statistic', name = 'homework_statistic'),
    url(r'^homework_notice$', 'Homework.views.homework_notice', name = 'homework_notice'),
    url(r'^achievement$', 'Homework.views.achievement', name="achievement"),
    # url(r'^statistic$')
]
