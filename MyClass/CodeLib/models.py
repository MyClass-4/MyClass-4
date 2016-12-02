# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
import hashlib
from User.models import User
from MyClass.settings import MEDIA_ROOT, BASE_DIR

# Create your views here.


@python_2_unicode_compatible
class CodeLib(models.Model):
	author = models.ForeignKey(User, verbose_name = '作者', related_name = 'user_set', null = True)
	code_name = models.CharField('代码名称', max_length = 100, default = "code.html")
	code = models.TextField('代码', default = "")

	def __str__(self):
		return self.code_name
	def __unicode__(self):
		return self.code_name
	class Meta:
		verbose_name = '代码库'
		verbose_name_plural = '代码库'
