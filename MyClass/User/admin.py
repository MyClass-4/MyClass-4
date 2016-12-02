# -*- coding:utf-8 -*-
from django.contrib import admin
import hashlib
from User.models import *
# Register your models here.

def encry_password(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

class UserAdmin(admin.ModelAdmin):
    list_display = ('number','name', 'avatar')
    filter_list = ('name')
    search_fields = ('name', 'number')
    # def save_model(self, request, obj, form, change):
    #     if change : #修改对象
    #         obj.password = encry_password(obj.password)
    #     obj.save()
    def delete_model(self, request, obj):
        obj.delete()

admin.site.register(User, UserAdmin)
