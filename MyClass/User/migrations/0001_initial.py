# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(default=b'/commonStatic/common_img/default_avatar.png', upload_to=b'/User/%Y/%m/%d/', max_length=250, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe5\xa4\xb4\xe5\x83\x8f')),
                ('name', models.CharField(default=b'guest', max_length=250, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('number', models.CharField(default=b'12345678', max_length=100, verbose_name=b'\xe5\xad\xa6\xe5\x8f\xb7')),
                ('password', models.CharField(default=b'e10adc3949ba59abbe56e057f20f883e', max_length=100, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
            ],
            options={
                'ordering': ['number', 'name'],
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
