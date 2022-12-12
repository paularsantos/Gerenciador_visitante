from django.urls import path

from django.contrib.auth import views as auth_views
from .views import UsuarioCreate

urlpartterns = [
    #path('', viemw, name='')
    path('login/', auth_views.LoginView.as_view(
        template_name = 'usuarios/login.html'
    ), name="login"),

    path('logout/', auth_views.LoginView.as_view(
        template_name = 'usuarios/logout.html'
    ), name="logout"),

    path('registrar/', UsuarioCreate.as_view(), name="registrar"),
]