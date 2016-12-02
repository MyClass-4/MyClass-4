# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20161124_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodeLib',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_name', models.CharField(default=b'code.html', max_length=100, verbose_name=b'\xe4\xbb\xa3\xe7\xa0\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('code', models.TextField(default=b'', verbose_name=b'\xe4\xbb\xa3\xe7\xa0\x81')),
                ('author', models.ForeignKey(related_name='user_set', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to='User.User', null=True)),
            ],
            options={
                'verbose_name': '\u4ee3\u7801\u5e93',
                'verbose_name_plural': '\u4ee3\u7801\u5e93',
            },
        ),
    ]
