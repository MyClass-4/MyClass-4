# -*- coding:utf-8 -*-
from django.contrib import admin
import hashlib
from Homework.models import *
import os
# from MyClass.wsgi import *
from MyClass import settings
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'teacher', 'grade')
    list_filter = ('course_name', 'grade', 'teacher')
    search_fields = ('course_name', 'grade', 'teacher')

class HomeworkAdmin(admin.ModelAdmin):
    list_filter = ('homework_type__course','homework_type','author')
    list_display = ('homework_type', 'author', 'source')
    def delete_model(self, request, obj):
        # print obj.source.name
        file_path = os.path.join(settings.MEDIA_ROOT, unicode(obj.source.name))
        if os.path.isfile(file_path) :
            os.remove(file_path)
        obj.delete()
    # list_display = ('homework_type', 'author', 'course')
    # list_filter = ('homework_type', 'author', 'course')
    # search_fields = ('homework_type', 'author', 'course')

class HomeworkTypeAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name', 'ddl')
    # list_filter = ('name', 'ddl')
    # search_fields = ('name', 'ddl')

admin.site.register(Course, CourseAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(HomeworkType, HomeworkTypeAdmin)
