# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0004_homework_homework_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeworktype',
            options={'ordering': ['name'], 'verbose_name': '\u4f5c\u4e1a\u7c7b\u578b', 'verbose_name_plural': '\u4f5c\u4e1a\u7c7b\u578b'},
        ),
        migrations.RemoveField(
            model_name='homeworktype',
            name='ddl',
        ),
    ]
