# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0007_auto_20150917_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificacaocadadm',
            name='requerente',
            field=models.CharField(default=1, max_length=50, choices=[('usuario', 'usuario'), ('proprietário', 'proprietario'), ('orgao judicial', 'orgao judicial'), ('outros', 'outros')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 17, 8, 45, 36, 212051), blank=True),
        ),
    ]
