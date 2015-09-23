# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pericia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequisitosAdm',
            fields=[
                ('numero_do_processo', models.OneToOneField(serialize=False, to='pericia.VerificacaoCadAdm', primary_key=True)),
                ('involucro', models.BooleanField(verbose_name='possui involucro: ')),
                ('numero_involucro', models.CharField(blank=True, max_length=10)),
                ('condicao_involucro', models.CharField(choices=[('conforme', 'conforme'), ('perfurado', 'perfurado'), ('lacre violado', 'lacre violado'), ('outros', 'outros')], max_length=30)),
                ('toi', models.BooleanField(verbose_name='possui toi: ')),
                ('idtoi', models.CharField(blank=True, max_length=50)),
                ('preenchimento_toi', models.CharField(choices=[('conforme', 'conforme'), ('incompleto', 'incompleto'), ('sem assinatura', 'sem assinatura'), ('outros', 'outros')], max_length=20)),
                ('integridade_lacre', models.CharField(choices=[('conforme', 'conforme'), ('ausente', 'ausente'), ('travas danificadas', 'travas danificadas'), ('arame rompido', 'arame rompido'), ('arame incorreto', 'arame incorreto'), ('ponto ligacao rompido', 'ponto ligacao rompido'), ('outros', 'outros')], max_length=20)),
                ('image_lacre', models.ImageField(blank=True, upload_to='imagens/verificacao/lacre/')),
                ('image_medidor', models.ImageField(blank=True, upload_to='imagens/verificacao/medidor/')),
                ('inspecao_visual', models.BooleanField(verbose_name='realizado? ')),
                ('dado_placa', models.BooleanField(verbose_name='esta conforme? ')),
                ('dimensao_medidor', models.BooleanField(verbose_name='esta conforme? ')),
                ('plano_selagem', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_inspecao_visual', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RequisitosMetrologicos',
            fields=[
                ('numero_do_processo', models.OneToOneField(serialize=False, to='pericia.VerificacaoCadAdm', primary_key=True)),
                ('energia_ativa_tensao', models.CharField(blank=True, max_length=10)),
                ('energia_ativa_corrente', models.CharField(blank=True, max_length=10)),
                ('energia_ativa_cos', models.CharField(blank=True, max_length=10)),
                ('energia_ativa_elementos', models.CharField(blank=True, max_length=20)),
                ('energia_ativa_erro', models.CharField(blank=True, max_length=10)),
                ('energia_ativa_erro_max', models.CharField(blank=True, max_length=20)),
                ('energia_reativa_tensao', models.CharField(blank=True, max_length=10)),
                ('energia_reativa_corrente', models.CharField(blank=True, max_length=10)),
                ('energia_reativa_cos', models.CharField(blank=True, max_length=10)),
                ('energia_reativa_elementos', models.CharField(blank=True, max_length=20)),
                ('energia_reativa_erro', models.CharField(blank=True, max_length=10)),
                ('energia_reativa_erro_max', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'ordering': ['numero_do_processo'],
                'verbose_name': 'verificacao',
                'verbose_name_plural': 'verificacoes',
            },
        ),
        migrations.CreateModel(
            name='RequisitosTecnicos',
            fields=[
                ('numero_do_processo', models.OneToOneField(serialize=False, to='pericia.VerificacaoCadAdm', primary_key=True)),
                ('ensaio_marcha_vazio', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_marcha_vazio', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_marcha_vazio', models.CharField(blank=True, max_length=50)),
                ('ensaio_mostrador', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_mostrador', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_mostrador', models.CharField(blank=True, max_length=50)),
                ('ensaio_exatidao', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_ensaio', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_exatidao', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='preliminaresinspecao',
            name='numero_do_processo',
        ),
        migrations.AlterField(
            model_name='verificacaocadadm',
            name='data_verificacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 8, 28, 23, 52, 43, 188816)),
        ),
        migrations.DeleteModel(
            name='PreliminaresInspecao',
        ),
    ]
