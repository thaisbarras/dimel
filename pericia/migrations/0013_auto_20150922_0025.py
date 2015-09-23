# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0012_auto_20150922_0024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadproprietario',
            options={'verbose_name_plural': 'proprietarios', 'ordering': ['id'], 'verbose_name': 'proprietario'},
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_retirada',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 25, 6, 280900)),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_visita_do_usuario',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 25, 6, 280900), blank=True),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_toi',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 25, 6, 282900), blank=True),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 25, 6, 282900), blank=True),
        ),
    ]
