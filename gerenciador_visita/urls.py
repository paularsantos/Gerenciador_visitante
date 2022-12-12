
from django.contrib import admin
from django.urls import path, include

from visitantes.views import (registrar_visitante, informacoes_visitante, finalizar_visita)
from dashboard.views import IndexView,InicioView
from usuarios.views import UsuarioCreate

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('dashboard.urls')),
    path('index/', IndexView.as_view(), name='index'),
    path('visitantes/registrar_visitantes/', registrar_visitante, name="registrar_visitantes"),
    path('', InicioView.as_view(), name='inicio'),
    path('usuarios/login/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'
    ), name='login'),
    path('usuarios/logout/', auth_views.LogoutView.as_view(
        template_name = 'usuarios/logout.html'
    ), name='logout'),
    path('visitantes/informacoes_visitante/<int:id>/', informacoes_visitante, name="informacoes_visitante"),
    path('visitantes/<int:id>/finalizar-visita', finalizar_visita, name="finalizar_visita"),
    path('registrar/', UsuarioCreate.as_view(), name="registrar"),
]
