# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0010_auto_20150922_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificacaocadadm',
            name='data_toi',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 21, 33, 213713), blank=True),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_retirada',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 21, 33, 211713)),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_visita_do_usuario',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 21, 33, 211713), blank=True),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 21, 33, 213713), blank=True),
        ),
    ]
