# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default=b'/static/common_img/default_avatar.png', upload_to=b'/User/%Y/%m/%d/', max_length=250, verbose_name=b'\xe4\xb8\xaa\xe4\xba\xba\xe5\xa4\xb4\xe5\x83\x8f'),
        ),
    ]
