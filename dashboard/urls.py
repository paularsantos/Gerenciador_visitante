from django.urls import path

from .views import PaginaInicial 
from dashboard.views import IndexView, InicioView

urlpatterns = [
    #path('admin/', admin.site.urls),
  path('base/',PaginaInicial.as_view(), name='base'),
  path('',InicioView.as_view(), name='inicio'),
  path('dashboard/index/', IndexView.as_view(), name='index',),
  
]