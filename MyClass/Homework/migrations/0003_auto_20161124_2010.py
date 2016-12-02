# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0002_auto_20161124_1956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['course', 'author'], 'verbose_name': '\u4f5c\u4e1a', 'verbose_name_plural': '\u4f5c\u4e1a'},
        ),
        migrations.RemoveField(
            model_name='homework',
            name='homework_type',
        ),
        migrations.AlterField(
            model_name='homework',
            name='author',
            field=models.ForeignKey(related_name='homework_author_set', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', blank=True, to='User.User', null=True),
        ),
    ]
