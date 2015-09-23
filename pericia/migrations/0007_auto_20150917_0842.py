# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0006_auto_20150916_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 17, 8, 42, 36, 761787)),
        ),
    ]
