# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0004_auto_20150916_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificacaocadadm',
            name='requerente',
            field=multiselectfield.db.fields.MultiSelectField(default=1, max_length=50, choices=[('usuario', 'usuario'), ('proprietário', 'proprietario'), ('orgao judicial', 'orgao judicial'), ('outros', 'outros')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 16, 21, 57, 33, 721640), blank=True),
        ),
    ]
