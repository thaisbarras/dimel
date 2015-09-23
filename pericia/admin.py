# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from pericia.models import CadTecnico, ProcedimentoPericia, CadEquipamento,\
    CadProprietario, CadMedidor, VerificacaoCadAdm, VerificacaoCadMedidor,\
    CadUsuario, CadRequerente, RequisitosAdm, RequisitosTecnicos,\
    RequisitosMetrologicos
from django.forms.widgets import CheckboxSelectMultiple

from django.forms import CheckboxSelectMultiple
    
class VerificacaoAdim(admin.ModelAdmin):
    formfield_overrides = {
                    models.ManyToManyField: {'widget': CheckboxSelectMultiple},
                        }

class UsuarioAdmin(admin.ModelAdmin):

    list_display = ('nome_tecnico',)
    list_filter = ('nome_tecnico',)

admin.site.register(CadUsuario)
admin.site.register(CadRequerente)
admin.site.register(CadProprietario)
admin.site.register(CadMedidor)
admin.site.register(CadEquipamento)

admin.site.register(ProcedimentoPericia)  # Use the default options
admin.site.register(CadTecnico, UsuarioAdmin)  # Use the customized options
#admin.site.register(CadTecnico)

admin.site.register(VerificacaoCadAdm)
admin.site.register(VerificacaoCadMedidor)
admin.site.register(RequisitosAdm)
admin.site.register(RequisitosTecnicos)
admin.site.register(RequisitosMetrologicos)
#admin.site.register(ProcedimentoPericia)