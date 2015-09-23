# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0008_auto_20150917_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 17, 9, 25, 51, 579202)),
        ),
    ]
