# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0005_auto_20161124_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeworktype',
            name='ddl',
            field=models.DateTimeField(null=True, verbose_name=b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='homeworktype',
            name='content',
            field=models.TextField(default=b'', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe8\xaf\xa6\xe6\x83\x85'),
        ),
    ]
