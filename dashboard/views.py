from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView
from visitantes.models import Visitante


from braces.views import GroupRequiredMixin



class PaginaInicial(GroupRequiredMixin, TemplateView):
    group_required = u'Porteiros', 'Condomino'
    template_name = "dashboard/base.html"




class InicioView(GroupRequiredMixin, TemplateView):
    group_required = u'Porteiros', 'Condomino'
    template_name = "dashboard/inicio.html"
    

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        context['nome_pagina'] = "Página Inicial"
        
        return context
    



class IndexView(GroupRequiredMixin,TemplateView):
    group_required = u'Porteiros'
    template_name = "dashboard/index.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        

        todos_visitantes = Visitante.objects.order_by(
            "-horario_chegada"
        )

        visitantes_aguardando = todos_visitantes.filter(
            status="AGUARDANDO"
        )

        visitantes_em_visita = todos_visitantes.filter(
            status="EM_VISITA"
        )

        visitantes_finalizado = todos_visitantes.filter(
            status="FINALIZADO"
        )

        hora_atual = timezone.now()
        mes_atual = hora_atual.month

        visitantes_mes = todos_visitantes.filter(
            horario_chegada__month = mes_atual
        )
        

        context = {
            "nome_pagina": "Painel de controle", 
            "todos_visitantes": todos_visitantes,
            "visitantes_aguardando": visitantes_aguardando.count(),
            "visitantes_em_visita": visitantes_em_visita.count(),
            "visitantes_finalizado": visitantes_finalizado.count(),
            "visitantes_mes": visitantes_mes.count(),
        }


        return context