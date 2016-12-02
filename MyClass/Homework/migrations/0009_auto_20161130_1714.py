# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0008_auto_20161130_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworktype',
            name='is_end_up',
            field=models.BooleanField(default=False, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f'),
        ),
    ]
