# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0005_auto_20150916_2157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='verificacaocadadm',
            name='requerente',
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 16, 22, 2, 22, 577162)),
        ),
    ]
