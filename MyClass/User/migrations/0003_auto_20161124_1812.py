# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_auto_20161124_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default=b'202cb962ac59075b964b07152d234b70', max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81'),
        ),
    ]
