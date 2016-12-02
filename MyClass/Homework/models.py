# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
import hashlib
from User.models import User
from MyClass.settings import MEDIA_ROOT, BASE_DIR
# Create your models here.

@python_2_unicode_compatible
class Course(models.Model):
    grade = models.CharField('年级', max_length = 20, default = '大一')
    teacher = models.CharField('授课老师', max_length = 50, default = '佚名')
    course_name = models.CharField('课程名称', max_length = 50, default = '')
    time = models.CharField('上课时间', max_length = 250, default = '')
    place = models.CharField('上课地点', max_length = 250, default = '')
    def __str__(self):
        return self.course_name
    def __unicode__(self):
        return self.course_name

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
        ordering = ['grade']

@python_2_unicode_compatible
class HomeworkType(models.Model):
    course = models.ForeignKey(Course, verbose_name = '课程', related_name = 'homeworktype_set',null = True) 
    name = models.CharField('作业名称', max_length = 250, default = '作业',)
    content = models.TextField('作业详情', default = '')
    ddl = models.DateTimeField('截止时间', editable = True, null = True)
    is_end_up = models.BooleanField('结束', default = False, blank = True)
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '作业类型'
        verbose_name_plural = '作业类型'
        ordering = ['name']


# redefine the upload_to function

def upload_to(instance, filename):
    return '/'.join([MEDIA_ROOT, 'Homework', instance.homework_type.course.course_name, instance.homework_type.name, filename])

@python_2_unicode_compatible
class Homework(models.Model):
    # course = models.ForeignKey(Course, verbose_name = '课程', related_name = 'homework_cource__set', null = True, blank = True)
    homework_type = models.ForeignKey(HomeworkType, verbose_name = '作业类型', related_name = 'homework_type_set', null = True)
    author = models.ForeignKey(User, verbose_name = '作者', related_name = 'homework_author_set', null = True, blank = True)
    source = models.FileField(upload_to = upload_to, verbose_name = '作业文件', default = 'media/Homework/default')
    def __str__(self):
        return unicode(self.homework_type) + ': ' + self.author.name
    def __unicode__(self):
        return unicode(self.homework_type) + ': ' + self.author.name

    class Meta:
        verbose_name = '作业'
        verbose_name_plural = '作业'
        ordering = ['homework_type__course','author']
