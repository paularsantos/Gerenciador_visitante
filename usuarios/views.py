
from django.db import models
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class Usuario(CreateView):

    def create_user(self, username, password=None):
        usuario = self.model(
            username=self(username)
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        if password:
            usuario.set_password(password)

        usuario.save()

        return usuario

    
class UsuarioCreate(CreateView):
    template_name = "usuarios/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        # Como aqui vem os dados do forms.py, não temos o form.instance e sim o form.cleaned_data
        # pegamos o nome do grupo que o usuário marcou no select e buscamos o objeto só para garantir 
        grupo = get_object_or_404(Group, name=form.cleaned_data['grupo'].name)

        # Aqui cria o usuário no banco
        url = super().form_valid(form)

        # Adiciona o grupo ao objeto usuário e salva
        self.object.groups.add(grupo)
        self.object.save()

        return url


    
    username = models.CharField(
        verbose_name="Nome do usuário", max_length=194, unique=True,
        
    )

    is_active = models.BooleanField(
        verbose_name="Usuário está ativo",
        default=False,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuário é da equipe de desenvolvimento",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuário é superusuario",
        default=False,
    )

    USERNAME = "username"

    objects = Usuario()

    class Meta:
        verbose_name = "Usuários"
        verbose_name_plural = "Usuários"
        db_table = "usuario"

    def __str__(self):
        return self.username
