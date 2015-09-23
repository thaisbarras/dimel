# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0014_auto_20150922_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_retirada',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 2, 4, 57, 36551)),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_visita_do_usuario',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 22, 2, 4, 57, 36551)),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_toi',
            field=models.DateField(blank=True, default=datetime.datetime(2015, 9, 22, 5, 4, 57, 37551, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateField(blank=True, default=datetime.datetime(2015, 9, 22, 5, 4, 57, 37551, tzinfo=utc)),
        ),
    ]
