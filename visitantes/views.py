from django.shortcuts import render, redirect, get_object_or_404
from time import timezone
from visitantes.models import Visitante
from visitantes.forms import VisitanteForm, AutorizaVisitanteForm
from django.contrib.auth.models import User
from django.contrib import messages
from braces.views import GroupRequiredMixin

from django.utils import timezone

from django.http import HttpResponseNotAllowed


def registrar_visitante(request):
    group_required = u'Porteiros', 'Condomino'

    form = VisitanteForm()

    if request.method == "POST":
        form = VisitanteForm(request.POST)

        
        if form.is_valid():
            visitante = form.save(commit=False)
            visitante.registrado_por = request.user
            visitante.save()

            messages.success(
                request,"visitante registrado com sucesso!"
            )

            return redirect("inicio")

    context = {
        "nome_pagina": "Registrar visitante",
        "form": form
    }

    return render(request, "visitantes/registrar_visitantes.html", context)


def informacoes_visitante(request, id):
    group_required = u'Porteiros'
    visitante = get_object_or_404(
        Visitante,
        id=id
    )

    form = AutorizaVisitanteForm()

    if request.method == "POST":
        form = AutorizaVisitanteForm(
            request.POST,
            instance=visitante
        )

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()

            visitante.save()

            messages.success(
                request,
                "Entrada do visitante autorizada com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Informações do visitante",
        "visitante": visitante,
        "form": form
    }

    return render(request, "visitantes/informacoes_visitante.html", context)



def finalizar_visita(request, id):

    if request.method == "POST":
        visitante = get_object_or_404(
            Visitante,
            id=id
        )

        visitante.status = "FINALIZADO"
        visitante.horario_saida = timezone.now()

        visitante.save()

        messages.success(
            request,
            "Visita finalizada com sucesso"
        )

        return redirect("index")

    else:
        return HttpResponseNotAllowed(
            ["POST"],
            "Método não permitido"
        )