# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('grade', models.CharField(default=b'\xe5\xa4\xa7\xe4\xb8\x80', max_length=20, verbose_name=b'\xe5\xb9\xb4\xe7\xba\xa7')),
                ('teacher', models.CharField(default=b'\xe4\xbd\x9a\xe5\x90\x8d', max_length=50, verbose_name=b'\xe6\x8e\x88\xe8\xaf\xbe\xe8\x80\x81\xe5\xb8\x88')),
                ('course_name', models.CharField(default=b'', max_length=50, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('time', models.CharField(default=b'', max_length=250, verbose_name=b'\xe4\xb8\x8a\xe8\xaf\xbe\xe6\x97\xb6\xe9\x97\xb4')),
                ('place', models.CharField(default=b'', max_length=250, verbose_name=b'\xe4\xb8\x8a\xe8\xaf\xbe\xe5\x9c\xb0\xe7\x82\xb9')),
            ],
            options={
                'ordering': ['grade'],
                'verbose_name': '\u8bfe\u7a0b',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('homework_name', models.CharField(default=b'\xe4\xbd\x9c\xe4\xb8\x9a', max_length=250, verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0')),
                ('source', models.FileField(default=b'media/Homework/default', upload_to=b'Homework/%Y/%m/%d', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe6\x96\x87\xe4\xbb\xb6')),
                ('author', models.ForeignKey(related_name='homework_set', verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', blank=True, to='User.User', null=True)),
                ('course', models.ForeignKey(related_name='homework_set', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b', blank=True, to='Homework.Course', null=True)),
            ],
            options={
                'ordering': ['course', 'homework_name', 'author'],
                'verbose_name': '\u4f5c\u4e1a',
                'verbose_name_plural': '\u4f5c\u4e1a',
            },
        ),
    ]
