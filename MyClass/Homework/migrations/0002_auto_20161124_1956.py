# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeworkType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'\xe4\xbd\x9c\xe4\xb8\x9a', max_length=250, verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe5\x90\x8d\xe7\xa7\xb0')),
                ('content', models.TextField(verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe8\xaf\xa6\xe6\x83\x85')),
                ('ddl', models.DateTimeField(null=True, verbose_name=b'\xe6\x88\xaa\xe6\xad\xa2\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-ddl', 'name'],
                'verbose_name': '\u4f5c\u4e1a\u7c7b\u578b',
                'verbose_name_plural': '\u4f5c\u4e1a\u7c7b\u578b',
            },
        ),
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['course', 'homework_type', 'author'], 'verbose_name': '\u4f5c\u4e1a', 'verbose_name_plural': '\u4f5c\u4e1a'},
        ),
        migrations.RemoveField(
            model_name='homework',
            name='homework_name',
        ),
        migrations.AlterField(
            model_name='homework',
            name='course',
            field=models.ForeignKey(related_name='homework_cource__set', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b', blank=True, to='Homework.Course', null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='homework_type',
            field=models.ForeignKey(related_name='homework_type_set', verbose_name=b'\xe4\xbd\x9c\xe4\xb8\x9a\xe7\xb1\xbb\xe5\x9e\x8b', blank=True, to='Homework.HomeworkType', null=True),
        ),
    ]
