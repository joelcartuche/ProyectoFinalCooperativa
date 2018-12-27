from django.urls import path

from . import views

urlpatterns = [
    path('',views.principal,name='principal'),
    path('gestion/',views.gestion_clientes,name='gestion'),
    path('crear/',views.crear_cliente,name='crear'),
    path(r'^modificar/(?P<pk>\d+)/$',views.modificar,name='modificar'),
    path(r'^eliminar/(?P<pk>\d+)/$',views.eliminar,name='eliminar'),
]
