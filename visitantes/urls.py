from django.urls import path

from visitantes.views import (registrar_visitante, informacoes_visitante, finalizar_visita)
from usuarios.views import UsuarioCreate

urlpartterns = [
    #path('admin/', admin.site.urls),
    path('visitantes/registrar_visitantes/', registrar_visitante, name="registrar_visitantes"),
    path('visitantes/informacoes_visitante/<int:id>/', informacoes_visitante, name="informacoes_visitante"),
    path('visitantes/<int:id>/finalizar-visita', finalizar_visita, name="finalizar_visita"),
]