# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0011_auto_20150922_0021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadproprietario',
            options={'verbose_name_plural': 'proprietarios', 'ordering': ['nome', 'id'], 'verbose_name': 'proprietario'},
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_retirada',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 24, 2, 236236)),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_visita_do_usuario',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 22, 0, 24, 2, 236236)),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_toi',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 22, 0, 24, 2, 238237)),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 22, 0, 24, 2, 238237)),
        ),
    ]
