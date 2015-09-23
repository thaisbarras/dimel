# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0013_auto_20150922_0025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadproprietario',
            options={'verbose_name': 'proprietario', 'verbose_name_plural': 'proprietarios', 'ordering': ['nome']},
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_retirada',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 2, 3, 13, 559633)),
        ),
        migrations.AlterField(
            model_name='agendamentomodel',
            name='data_visita_do_usuario',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 22, 2, 3, 13, 559633), blank=True),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_toi',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 2, 3, 13, 561633), blank=True),
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateField(default=datetime.datetime(2015, 9, 22, 2, 3, 13, 560633), blank=True),
        ),
    ]
