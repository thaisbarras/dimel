# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadEquipamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('equipamento_calibrado', models.CharField(max_length=20)),
                ('data_calibracao', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'equipamento',
                'ordering': ['equipamento_calibrado'],
                'verbose_name_plural': 'equipamentos',
            },
        ),
        migrations.CreateModel(
            name='CadMedidor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('fabricante_marca_medidor', models.CharField(max_length=20)),
                ('modelo_medidor', models.CharField(max_length=20)),
                ('pam', models.CharField(max_length=20)),
                ('classe', models.CharField(max_length=20)),
                ('num_elementos', models.CharField(max_length=20)),
                ('num_fios', models.CharField(max_length=20)),
                ('tensao_nominal_v', models.CharField(max_length=20)),
                ('corrente_nominal_max_a', models.CharField(max_length=20)),
                ('frequencia_nominal', models.CharField(max_length=20)),
                ('constante', models.CharField(max_length=20)),
                ('ano_fabricacao', models.CharField(max_length=20)),
                ('identificacao', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'medidor',
                'ordering': ['fabricante_marca_medidor'],
                'verbose_name_plural': 'medidores',
            },
        ),
        migrations.CreateModel(
            name='CadProprietario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('representante_legal', models.CharField(max_length=50)),
                ('cpf_cnpf_representante', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'proprietario',
                'ordering': ['nome'],
                'verbose_name_plural': 'proprietarios',
            },
        ),
        migrations.CreateModel(
            name='CadRequerente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'requerente',
                'ordering': ['nome'],
                'verbose_name_plural': 'requerentes',
            },
        ),
        migrations.CreateModel(
            name='CadTecnico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome_tecnico', models.CharField(max_length=20)),
                ('identificacao_tecnico', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'tecnico',
                'ordering': ['nome_tecnico'],
                'verbose_name_plural': 'tecnicos',
            },
        ),
        migrations.CreateModel(
            name='CadUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=50)),
                ('endereco', models.CharField(max_length=40)),
                ('cpf_cnpj', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'verbose_name': 'usuario',
                'ordering': ['nome'],
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='ProcedimentoPericia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('image_pericia', models.ImageField(upload_to='imagens/pericia/medidor/', blank=True)),
                ('data_pericia', models.DateTimeField()),
                ('tampa_medidor', models.CharField(choices=[('conforme', 'conforme'), ('tampa quebrada', 'tampa quebrada'), ('tampa perfurada', 'tampa perfurada'), ('tampa deformada', 'tampa deformada'), ('sem tampa', 'sem tampa'), ('Outros', 'Outros')], max_length=50)),
                ('base_medidor', models.CharField(choices=[('conforme', 'conforme'), ('base quebrada', 'base quebrada'), ('base perfurada', 'base perfurada'), ('base deformada', 'base deformada'), ('base adulterada', 'base adulterada'), ('Outros', 'Outros')], max_length=50)),
                ('bloco_terminais_medidor', models.CharField(choices=[('conforme', 'conforme'), ('bloco de terminais quebrada', 'bloco de terminais quebrada'), ('ausencia de parafuso', 'ausencia de parafuso'), ('parafuso oxidado', 'parafuso oxidado'), ('Terminais de prova abertos', 'Terminais de prova abertos'), ('Outros', 'Outros')], max_length=50)),
                ('suporte_parafuso', models.CharField(choices=[('conforme', 'conforme'), ('nao aplicavel', 'nao aplicavel'), ('suporte perfurado', 'suporte perfurado'), ('suporte deformado', 'suporte deformado'), ('material de gaveta deteriorado', 'material de gaveta deteriorado'), ('Outros', 'Outros')], max_length=50)),
                ('circuito_corrente', models.CharField(choices=[('conforme', 'conforme'), ('curto circuito', 'curto circuito'), ('fio rompido', 'fio rompido'), ('Outros', 'Outros')], max_length=50)),
                ('circuito_tensao', models.CharField(choices=[('conforme', 'conforme'), ('descontinuidade', 'descontinuidade'), ('fio rompido', 'fio rompido'), ('introducao de componentes', 'introducao de componentes'), ('Outros', 'Outros')], max_length=50)),
                ('mostrador', models.CharField(choices=[('conforme', 'conforme'), ('desconectado ou deslocado', 'desconectado ou deslocado '), ('mostrador danificada ', 'mostrador modificado'), ('engrenagens danificadas', 'engrenagens danificadas '), ('mostrador apagado ', 'mostrador apagado'), ('segmentos defeituosos', 'segmentos defeituosos'), ('noo indica grandeza', 'noo indica grandeza'), ('outros', 'outros')], max_length=50)),
                ('placa_identficacao', models.CharField(choices=[('conforme', 'conforme'), ('impressao adulterada', 'impressao adulterada'), ('outros', 'outros')], max_length=50)),
                ('placa_circuito_impresso_componetes', models.CharField(choices=[('conforme', 'conforme'), ('introducao de componentes', 'introducao de componentes'), ('conforme', 'conforme'), ('Retirada de componentes', 'Retirada de componentes'), ('Trilhas raspadas', 'Trilhas raspadas'), ('curto circuito', 'curto circuito'), ('introdução de circuitos', 'introdução de circuitos'), ('soldas defeituosas', 'soldas defeituosas'), ('outros', 'outros')], max_length=50)),
                ('outros', models.CharField(choices=[('nao aplicavel', 'nao aplicavel'), ('presenca de corpo estranho no interior do medidor', 'presenca de corpo estranho no interior do medidor'), ('presenca de sujeira no interior do medidor', 'presenca de sujeira no interior do medidor'), ('presenca de insetos no interior do medidor', 'presenca de insetos no interior do medidor'), ('botoes danificados', 'botoes danificados'), ('outros', 'outros')], max_length=60)),
                ('involucro_devolucao', models.BooleanField(verbose_name='possui? ')),
                ('pendencias', models.BooleanField(verbose_name='possui? ')),
                ('obs', models.CharField(max_length=500, blank=True)),
            ],
            options={
                'verbose_name': 'pericia',
                'ordering': ['verificacao'],
                'verbose_name_plural': 'pericias',
            },
        ),
        migrations.CreateModel(
            name='VerificacaoCadAdm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('processo', models.CharField(max_length=10)),
                ('data_verificacao', models.DateTimeField(blank=True, default=datetime.datetime(2015, 8, 28, 22, 44, 5, 13270))),
                ('local', models.CharField(max_length=100)),
                ('temperatura_ambiente', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'verificacaoadm',
                'ordering': ['processo'],
                'verbose_name_plural': 'verificacoesadm',
            },
        ),
        migrations.CreateModel(
            name='PreliminaresInspecao',
            fields=[
                ('numero_do_processo', models.OneToOneField(primary_key=True, to='pericia.VerificacaoCadAdm', serialize=False)),
                ('involucro', models.BooleanField(verbose_name='possui involucro: ')),
                ('numero_involucro', models.CharField(max_length=10, blank=True)),
                ('condicao_involucro', models.CharField(choices=[('conforme', 'conforme'), ('perfurado', 'perfurado'), ('lacre violado', 'lacre violado'), ('outros', 'outros')], max_length=30)),
                ('toi', models.BooleanField(verbose_name='possui toi: ')),
                ('idtoi', models.CharField(max_length=50, blank=True)),
                ('preenchimento_toi', models.CharField(choices=[('conforme', 'conforme'), ('incompleto', 'incompleto'), ('sem assinatura', 'sem assinatura'), ('outros', 'outros')], max_length=20)),
                ('integridade_lacre', models.CharField(choices=[('conforme', 'conforme'), ('ausente', 'ausente'), ('travas danificadas', 'travas danificadas'), ('arame rompido', 'arame rompido'), ('arame incorreto', 'arame incorreto'), ('ponto ligacao rompido', 'ponto ligacao rompido'), ('outros', 'outros')], max_length=20)),
                ('image_lacre', models.ImageField(upload_to='imagens/verificacao/lacre/', blank=True)),
                ('image_medidor', models.ImageField(upload_to='imagens/verificacao/medidor/', blank=True)),
                ('inspecao_visual', models.BooleanField(verbose_name='realizado? ')),
                ('dado_placa', models.BooleanField(verbose_name='esta conforme? ')),
                ('dimensao_medidor', models.BooleanField(verbose_name='esta conforme? ')),
                ('plano_selagem', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_inspecao_visual', models.CharField(max_length=50, blank=True)),
                ('ensaio_marcha_vazio', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_marcha_vazio', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_marcha_vazio', models.CharField(max_length=50, blank=True)),
                ('ensaio_mostrador', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_mostrador', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_mostrador', models.CharField(max_length=50, blank=True)),
                ('ensaio_exatidao', models.BooleanField(verbose_name='realizado? ')),
                ('resultado_ensaio_ensaio', models.BooleanField(verbose_name='esta conforme? ')),
                ('obs_ensaio_exatidao', models.CharField(max_length=50, blank=True)),
                ('energia_ativa_tensao', models.CharField(max_length=10, blank=True)),
                ('energia_ativa_corrente', models.CharField(max_length=10, blank=True)),
                ('energia_ativa_cos', models.CharField(max_length=10, blank=True)),
                ('energia_ativa_elementos', models.CharField(max_length=20, blank=True)),
                ('energia_ativa_erro', models.CharField(max_length=10, blank=True)),
                ('energia_ativa_erro_max', models.CharField(max_length=20, blank=True)),
                ('energia_reativa_tensao', models.CharField(max_length=10, blank=True)),
                ('energia_reativa_corrente', models.CharField(max_length=10, blank=True)),
                ('energia_reativa_cos', models.CharField(max_length=10, blank=True)),
                ('energia_reativa_elementos', models.CharField(max_length=20, blank=True)),
                ('energia_reativa_erro', models.CharField(max_length=10, blank=True)),
                ('energia_reativa_erro_max', models.CharField(max_length=20, blank=True)),
            ],
            options={
                'verbose_name': 'verificacao',
                'ordering': ['numero_do_processo'],
                'verbose_name_plural': 'verificacoes',
            },
        ),
        migrations.CreateModel(
            name='VerificacaoCadMedidor',
            fields=[
                ('numero_do_processo', models.OneToOneField(primary_key=True, to='pericia.VerificacaoCadAdm', serialize=False)),
                ('tipo_medidor', models.CharField(choices=[('medidor_eletroeletronico', 'medidor_eletroeletronico'), ('medidor_eletromecanico', 'medidor_eletromecanico')], max_length=30)),
                ('classe_do_medidor', models.CharField(max_length=10)),
                ('numero_de_elementos', models.CharField(max_length=10)),
                ('numero_de_fios', models.CharField(max_length=10)),
                ('tensao_nominal', models.CharField(max_length=10)),
                ('corrente_nominal_max_a', models.CharField(max_length=10)),
                ('frequencia_nominal', models.CharField(max_length=10)),
                ('constante', models.CharField(max_length=10)),
                ('ano_de_fabricante', models.CharField(max_length=10)),
                ('identificacao', models.CharField(max_length=10)),
                ('leitura_inicial_medidor', models.CharField(max_length=10)),
                ('leitura_final_medidor', models.CharField(max_length=10)),
                ('medidor', models.ForeignKey(related_name='medidor', to='pericia.CadMedidor')),
            ],
            options={
                'verbose_name': 'cadmedidor',
                'ordering': ['medidor'],
                'verbose_name_plural': 'cadmedidores',
            },
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='equipamentos_utilizados',
            field=models.ManyToManyField(related_name='equipamento', to='pericia.CadEquipamento'),
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='proprietario',
            field=models.ForeignKey(to='pericia.CadProprietario'),
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='requerente',
            field=models.ForeignKey(to='pericia.CadRequerente'),
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='tecnico_verificacao',
            field=models.ForeignKey(related_name='tecnico', to='pericia.CadTecnico'),
        ),
        migrations.AddField(
            model_name='verificacaocadadm',
            name='usuario',
            field=models.ForeignKey(to='pericia.CadUsuario'),
        ),
        migrations.AddField(
            model_name='procedimentopericia',
            name='verificacao',
            field=models.ForeignKey(to='pericia.VerificacaoCadAdm'),
        ),
    ]
