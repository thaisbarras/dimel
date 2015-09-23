# -*- encoding: utf8 -*-
#from pericia.models import VerificacaoCadAdm
#from django.template.context import RequestContext
#from django.shortcuts import render, redirect, render_to_response, get_object_or_404
#from pericia.forms import FormItemPericia
#from django.http.response import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import ProcedimentoPericia
from pericia.forms import ProcedimentoPericiaContactForm,\
    ProcedimentoPericiaForm, PreliminaresInspecaoForm, VerificacaoCadAdmForm
from django.views.generic.list import ListView
from django.contrib.redirects.models import Redirect
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import DeleteView, UpdateView
from django.template.context import RequestContext
from pericia.models import VerificacaoCadAdm, VerificacaoCadMedidor, RequisitosTecnicos,\
    RequisitosAdm, RequisitosMetrologicos, AgendamentoModel
from vanilla import CreateView

#from .forms import PericiaContactForm


def home(request):
    return render(request, 'home.html')


class Lista(ListView):
        template_name = 'bands/pericia_listing.html'
        model = ProcedimentoPericia
        #fields = ['numero_pericia', 'verificacao', 'tampa_medidor', 'base_medidor', 'bloco_terminais_medidor']
        context_object = 'verificacao'
        
class ListaVerificacao(ListView):
        template_name = 'bands/verificacao_listing.html'
        model = VerificacaoCadAdm
        #fields = ['numero_pericia', 'verificacao', 'tampa_medidor', 'base_medidor', 'bloco_terminais_medidor']
        context_object = 'processo'

class ListaAgendamento (ListView):
    template_name = 'bands/agendamentos.html'
    model = AgendamentoModel
    context_object = 'agendamento'

@login_required(login_url='/accounts/login/')
def pericia_detail(request, pk):
    item = get_object_or_404(ProcedimentoPericia, pk=pk)
    form = ProcedimentoPericiaForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/pericias")
    return render(request, "bands/pericia_detail.html", {'form': form})

def verificacao_detail(request, pk):
    item = get_object_or_404(VerificacaoCadAdm, pk=pk)
    form = PreliminaresInspecaoForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/verificacoes")
    return render(request, "bands/verificacao_detail.html", {'form': form})
    
def adiciona_verificacao(request):
    if request.method == "POST":
        form = PreliminaresInspecaoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response("bands/verificacao_confirm.html")
    else:
        form = PreliminaresInspecaoForm()
    return render_to_response("bands/verificacao_adiciona.html", {'form': form},
        context_instance=RequestContext(request))

class PericiaForm(CreateView):
    template_name = 'bands/pericia_form.html'
    model = ProcedimentoPericia
    fields = ['verificacao', 'image_pericia', 'data_pericia', 'tampa_medidor', 'base_medidor', 'bloco_terminais_medidor', 'suporte_parafuso', 'circuito_corrente', 'circuito_tensao', 'mostrador', 'placa_identficacao', 'placa_circuito_impresso_componetes', 'outros', 'involucro_devolucao', 'pendencias', 'obs']
    success_url = reverse_lazy('lista')


class AgendamentoAdd(CreateView): 
    template_name = 'bands/agendamento_add.html'
    model = AgendamentoModel
    #form_class = VerificacaoCadAdmForm
    fields = '__all__'
    success_url = reverse_lazy('lista_agendamento')

 
class VerificacaoFormAdm(CreateView): 
    template_name = 'bands/verificacao_form_adm.html'
    model = VerificacaoCadAdm
    form_class = VerificacaoCadAdmForm
    #fields = ['processo', 'data_verificacao', 'local', 'temperatura_ambiente', 'usuario', 'proprietario', 'requerente', 'tecnico_verificacao', 'equipamentos_utilizados']
    success_url = reverse_lazy('verificacao_form_medidor')
    

class VerificacaoFormMedidor(CreateView): 
    template_name = 'bands/verificacao_form_medidor.html'
    model = VerificacaoCadMedidor
    fields = ['numero_do_processo', 'medidor', 'tipo_medidor', 'classe_do_medidor', 'numero_de_elementos', 'numero_de_fios', 'tensao_nominal', 'corrente_nominal_max_a', 'frequencia_nominal', 'constante', 'ano_de_fabricante', 'identificacao', 'leitura_inicial_medidor', 'leitura_final_medidor']
    success_url = reverse_lazy('verificacao_requisitosadm')

class RequisitosAdmForm(CreateView):    
    template_name = 'bands/verificacao_requisitosadm.html'
    model = RequisitosAdm
    fields = ['numero_do_processo', 'involucro', 'numero_involucro', 'condicao_involucro', 'toi', 'idtoi', 'preenchimento_toi', 'integridade_lacre', 'image_lacre', 'image_medidor','inspecao_visual', 'dado_placa', 'dimensao_medidor', 'plano_selagem', 'obs_inspecao_visual']
    success_url = reverse_lazy('verificacao_requisitostecnicos')

class RequisitosTecnicosForm(CreateView):    
    template_name = 'bands/verificacao_requisitostecnicos.html'
    model = RequisitosTecnicos
    fields = ['ensaio_marcha_vazio', 'resultado_ensaio_marcha_vazio', 'obs_ensaio_marcha_vazio', 'ensaio_mostrador', 'resultado_ensaio_mostrador', 'obs_ensaio_mostrador', 'ensaio_exatidao', 'resultado_ensaio_ensaio', 'obs_ensaio_exatidao']
    success_url = reverse_lazy('verificacao_requisitosmetrologicos')

'''    
class RequisitosTecnicosForm(CreateView):    
    model = RequisitosTecnicos
    success_url = reverse_lazy('verificacao_requisitosmetrologicos')
'''
class RequisitosMetrologicosForm(CreateView):    
    template_name = 'bands/verificacao_requisitosmetrologicos.html'
    model = RequisitosMetrologicos
    fields = ['energia_ativa_tensao', 'energia_ativa_corrente', 'energia_ativa_cos', 'energia_ativa_elementos', 'energia_ativa_erro', 'energia_ativa_erro_max', 'energia_reativa_tensao', 'energia_reativa_corrente', 'energia_reativa_cos', 'energia_reativa_elementos', 'energia_reativa_erro', 'energia_reativa_erro_max']
    success_url = reverse_lazy('listaverificacao')
    
'''class VerificacaoForm(CreateView):    
    template_name = 'bands/verificacao_form.html'
    model = VerificacaoCadAdm
    fields = ['energia_ativa_tensao', 'energia_ativa_corrente', 'energia_ativa_cos', 'energia_ativa_elementos', 'energia_ativa_erro', 'energia_ativa_erro_max', 'energia_reativa_tensao', 'energia_reativa_corrente', 'energia_reativa_cos', 'energia_reativa_elementos', 'energia_reativa_erro', 'energia_reativa_erro_max']
    success_url = reverse_lazy('listaverificacao')
'''

class VerificacaoDel(DeleteView):
    template_name = 'bands/verificacao_del_form.html'
    model = VerificacaoCadAdm
    success_url = reverse_lazy('listaverificacao')
    
class PericiaDel(DeleteView):
    template_name = 'bands/pericia_del_form.html'
    model = ProcedimentoPericia
    success_url = reverse_lazy('lista')
    

class PericiaUpdate(UpdateView):
    template_name = 'bands/pericia_detail.html'
    model = ProcedimentoPericia
    fields = ['verificacao', 'image_pericia', 'data_pericia', 'tampa_medidor', 'base_medidor', 'bloco_terminais_medidor', 'suporte_parafuso', 'circuito_corrente', 'circuito_tensao', 'mostrador', 'placa_identficacao', 'placa_circuito_impresso_componetes', 'outros', 'involucro_devolucao', 'pendencias', 'obs']
    success_url = reverse_lazy('lista')
    
class VerificacaoUpdate(UpdateView):
    template_name = 'bands/verificacao_detail.html'
    model = VerificacaoCadAdm
    #fields = ['processo', 'proprietario', 'tecnico_verificacao', 'equipamento_utilzado', 'medidor', 'leitura_inicial_medidor', 'leitura_final_medidor', 'documento_referencia', 'local', 'data', 'temperatura', 'involucro', 'numero_involucro', 'condicao_involucro', 'toi', 'idtoi', 'preenchimento_toi', 'integridade_lacre', 'image_lacre', 'image_medidor','inspecao_visual', 'dado_placa', 'dimensao_medidor', 'plano_selagem', 'obs_inspecao_visual', 'ensaio_marcha_vazio', 'resultado_ensaio_marcha_vazio', 'obs_ensaio_marcha_vazio', 'ensaio_mostrador', 'resultado_ensaio_mostrador', 'obs_ensaio_mostrador', 'ensaio_exatidao', 'resultado_ensaio_ensaio', 'obs_ensaio_exatidao', 'energia_ativa_tensao', 'energia_ativa_corrente', 'energia_ativa_cos', 'energia_ativa_elementos', 'energia_ativa_erro', 'energia_ativa_erro_max', 'energia_reativa_tensao', 'energia_reativa_corrente', 'energia_reativa_cos', 'energia_reativa_elementos', 'energia_reativa_erro', 'energia_reativa_erro_max']
    fields = '__all__'
    success_url = reverse_lazy('listaverificacao')
    
class VerificacaoCadMedidorUpdate(UpdateView):
    template_name = 'bands/verificacaomedidor_detail.html'
    model = VerificacaoCadMedidor
    #fields = ['processo', 'proprietario', 'tecnico_verificacao', 'equipamento_utilzado', 'medidor', 'leitura_inicial_medidor', 'leitura_final_medidor', 'documento_referencia', 'local', 'data', 'temperatura', 'involucro', 'numero_involucro', 'condicao_involucro', 'toi', 'idtoi', 'preenchimento_toi', 'integridade_lacre', 'image_lacre', 'image_medidor','inspecao_visual', 'dado_placa', 'dimensao_medidor', 'plano_selagem', 'obs_inspecao_visual', 'ensaio_marcha_vazio', 'resultado_ensaio_marcha_vazio', 'obs_ensaio_marcha_vazio', 'ensaio_mostrador', 'resultado_ensaio_mostrador', 'obs_ensaio_mostrador', 'ensaio_exatidao', 'resultado_ensaio_ensaio', 'obs_ensaio_exatidao', 'energia_ativa_tensao', 'energia_ativa_corrente', 'energia_ativa_cos', 'energia_ativa_elementos', 'energia_ativa_erro', 'energia_ativa_erro_max', 'energia_reativa_tensao', 'energia_reativa_corrente', 'energia_reativa_cos', 'energia_reativa_elementos', 'energia_reativa_erro', 'energia_reativa_erro_max']
    fields = '__all__'
    success_url = reverse_lazy('listaverificacao')
    


@login_required(login_url='/accounts/login/')
def protected_view(request):
    """ A view that can only be accessed by logged-in users """
    return render(request, 'bands/protected.html', {'current_user': request.user})

def pericia_contact(request):
    """ A example of form """
    if request.method == 'POST':
        form = ProcedimentoPericiaContactForm(request.POST)
    else:
        form = ProcedimentoPericiaContactForm()
    return render(request, 'bands/pericia_contact.html', {'form': form})

def message(request):
    """ Message if is not authenticated. Simple view! """
    return HttpResponse('Access denied!')


'''
def index(request):
    lista_itens = VerificacaoCadAdm.objects.all()
    return render(request, "lista.html", {'lista_itens': lista_itens})

def adiciona(request):
    if request.method == "POST":
        form = FormItemPericia(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render_to_response('salvo.html', {})
    else:
        form = FormItemPericia()
    return render_to_response("adiciona.html", {'form': form},
        context_instance=RequestContext(request))
    

def item(request, nr_item):
    item = get_object_or_404(VerificacaoCadAdm, pk=nr_item)
    form = FormItemPericia(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, "item.html", {'form': form})
    
def remove(request, nr_item):
    item = get_object_or_404(VerificacaoCadAdm, pk=nr_item)
    if request.method =="POST":
        item.delete()
        return render_to_response("removido.html", {})
        
    return render(request, "remove.html", {'item': item})
'''

""" 
def pericia_listing(request): 
   A view of all pericias. 
    pericias = ProcedimentoPericia.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        pericias = pericias.filter(name__icontains=var_get_search)
    return render(request, 'bands/pericia_listing.html', {'pericias': pericias})"""
    
"""def pericia_detail(request, pk):
   A view of all members by pericias.
    pericia = get_object_or_404(ProcedimentoPericia, pk=pk)
    #verificacao = VerificacaoCadAdm.objects.all().filter(pericia=pericia)
    context = {'pericia': pericia}
    return render(request, 'bands/pericia_detail.html', context) """    



    
