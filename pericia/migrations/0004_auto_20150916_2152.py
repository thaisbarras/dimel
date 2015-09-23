# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0003_auto_20150916_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verificacaocadadm',
            name='requerente',
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 21, 52, 33, 278456), blank=True),
        ),
    ]
