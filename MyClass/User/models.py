#-*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
import hashlib
# Create your models here.

def encry_password(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

@python_2_unicode_compatible
class User(models.Model):
    avatar = models.ImageField(upload_to = 'User/%Y/%m/%d/', verbose_name = '个人头像', max_length = 250, default = '/static/common_img/default_avatar.png')
    name = models.CharField('名字', max_length = 250, default = 'guest')
    number = models.CharField('学号', max_length = 100, default = '12345678')
    password = models.CharField('密码', max_length = 100, default = encry_password('123456'))
    def __str__(self):
        return self.name
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['number', 'name']
