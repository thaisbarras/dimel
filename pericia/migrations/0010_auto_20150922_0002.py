# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0009_auto_20150917_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendamentoModel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('codigo_agendamento', models.CharField(max_length=10)),
                ('data_retirada', models.DateTimeField(default=datetime.datetime(2015, 9, 22, 0, 2, 10, 217193))),
                ('data_visita_do_usuario', models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 22, 0, 2, 10, 217193))),
                ('usuario_compareceu', models.CharField(choices=[('sim', 'sim'), ('nao', 'nao')], max_length=50)),
                ('observacoes', models.CharField(max_length=100)),
                ('codigo_usuario', models.ForeignKey(to='pericia.CadUsuario')),
            ],
            options={
                'ordering': ['codigo_agendamento'],
                'verbose_name': 'agendamento',
                'verbose_name_plural': 'agendamentos',
            },
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 9, 22, 0, 2, 10, 218193)),
        ),
    ]
