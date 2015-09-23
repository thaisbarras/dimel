# -*- coding: utf-8 -*-
"""inmetro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
#from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import include, url
from pericia.views import PericiaForm, Lista, ListaVerificacao,\
    VerificacaoDel, PericiaDel, PericiaUpdate, VerificacaoUpdate,\
    VerificacaoFormAdm, VerificacaoFormMedidor, RequisitosTecnicosForm,\
    RequisitosAdmForm, RequisitosMetrologicosForm, ListaAgendamento,\
    AgendamentoAdd, VerificacaoCadMedidorUpdate

urlpatterns = [    
    #'inmetro.pericia.views',
    url(r'^$', 'pericia.views.home', name='home'),
    #url(r'^pericias/$', 'pericia.views.pericia_listing', name='pericias'),
    url(r'^pericias/$', Lista.as_view(), name='lista'),
    url(r'^verificacoes/$', ListaVerificacao.as_view(), name='listaverificacao'),
    url(r'^agendamentos/$', ListaAgendamento.as_view(), name='lista_agendamento'),
    #url(r'^verificacoes/(?P<pk>\d+)/$', 'pericia.views.verificacao_detail', name='verificacao_detail'),
    #url(r'^pericias/(?P<pk>\d+)/$', 'pericia.views.pericia_detail', name='pericia_detail'),
    url(r'^verificacoes/(?P<pk>\d+)/$', VerificacaoUpdate.as_view(), name='verificacao_detail'),
    url(r'^medidores/(?P<pk>\d+)/$', VerificacaoCadMedidorUpdate.as_view(), name='medidor_detail'),
    url(r'^pericias/(?P<pk>\d+)/$', PericiaUpdate.as_view(), name='pericia_detail'),
    url(r'^verificacoesdel/(?P<pk>\d+)/$', VerificacaoDel.as_view(), name='verificacao_del'),
    url(r'^periciadel/(?P<pk>\d+)/$', PericiaDel.as_view(), name='pericia_del'),
    url(r'^pericia_form/$', PericiaForm.as_view(), name='pericia_form'),
    #url(r'^verificacao_form/$', VerificacaoForm.as_view(), name='verificacao_form'),
    url(r'^agendamento_add/$', AgendamentoAdd.as_view(), name='agendamento_add'),
    url(r'^verificacao_form_adm/$', VerificacaoFormAdm.as_view(), name='verificacao_form_adm'),
    url(r'^verificacao_form_medidor/$', VerificacaoFormMedidor.as_view(), name='verificacao_form_medidor'),
    url(r'^verificacao_requisitosadm/$', RequisitosAdmForm.as_view(), name='verificacao_requisitosadm'),
    url(r'^verificacao_requisitostecnicos/$', RequisitosTecnicosForm.as_view(), name='verificacao_requisitostecnicos'),
    url(r'^verificacao_requisitosmetrologicos/$', RequisitosMetrologicosForm.as_view(), name='verificacao_requisitosmetrologicos'),
    #url(r'^verificacao_form/$', 'pericia.views.adiciona_verificacao', name='verificacao_form'),
    
    url(r'^contact/$', 'pericia.views.pericia_contact', name='contact'),
    url(r'^protected/$', 'pericia.views.protected_view', name='protected'),
    #url(r'^accounts/login/$', 'message'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
]