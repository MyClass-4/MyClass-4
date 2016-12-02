# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Homework.models


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0006_auto_20161124_2017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['author'], 'verbose_name': '\u4f5c\u4e1a', 'verbose_name_plural': '\u4f5c\u4e1a'},
        ),
        migrations.RemoveField(
            model_name='homework',
            name='course',
        ),
        migrations.AddField(
            model_name='homeworktype',
            name='course',
            field=models.ForeignKey(related_name='homeworktype_set', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b', to='Homework.Course', null=True),
        ),
        migrations.AddField(
            model_name='homeworktype',
            name='is_end_up',
            field=models.BooleanField(default=True, verbose_name=b'\xe7\xbb\x93\xe6\x9d\x9f'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='homework_type',
            field=models.ForeignKey(related_name='homework_type_set', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b', to='Homework.HomeworkType', null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='source',
            field=models.FileField(default=b'media/Homework/default', upload_to=Homework.models.upload_to, verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe6\x96\x87\xe4\xbb\xb6'),
        ),
    ]
