# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0003_auto_20161124_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='homework_type',
            field=models.ForeignKey(related_name='homework_type_set', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b', blank=True, to='Homework.HomeworkType', null=True),
        ),
    ]
