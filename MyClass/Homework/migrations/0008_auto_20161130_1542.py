# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0007_auto_20161130_1507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['homework_type__course', 'author'], 'verbose_name': '\u4f5c\u4e1a', 'verbose_name_plural': '\u4f5c\u4e1a'},
        ),
    ]
