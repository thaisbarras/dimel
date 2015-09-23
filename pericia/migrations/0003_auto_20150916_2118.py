# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0002_auto_20150828_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 21, 18, 37, 364792), blank=True),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='requerente',
            field=models.CharField(choices=[('usuario', 'usuario'), ('proprietário', 'proprietario'), ('orgao judicial', 'orgao judicial'), ('outros', 'outros')], max_length=50),
        ),
    ]
