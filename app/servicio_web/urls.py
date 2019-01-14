from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('listaClientes/',views.listaCliente.as_view()),
    path('listaCuentas/',views.listaCuenta.as_view()),
    path('listaTransacciones/',views.listaTransaccion.as_view()),
    path('busquedaCliente/',views.busquedaCliente.as_view()),
    path('busquedaCuenta/',views.busquedaCuenta.as_view()),
    path('busquedaTransaccion/',views.busquedaTransaccion.as_view()),
]
