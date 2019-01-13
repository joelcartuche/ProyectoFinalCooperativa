from django.urls import path

from . import views

urlpatterns = [
    path('',views.principal,name='principal'),
    path('gestion/',views.gestion_clientes,name='gestion'),
    path('crear/',views.crear_cliente,name='crear'),
    path(r'^modificar/(?P<pk>\d+)/$',views.modificar,name='modificar'),
    path(r'^eliminar/(?P<pk>\d+)/$',views.eliminar,name='eliminar'),
    path(r'^activar/(?P<pk>\d+)/$',views.activar,name='activar'),
    path('listadepositoBuscar',views.listarClienteCuentaBusqueda,name='listaDepositoBuscar'),
    path('transferencia/',views.transferenciaLista,name='transferenciaLista'),
    path('listaClienteCuenta/',views.listarClienteCuenta,name='listaClienteCuenta'),
    path('confirmarContra/',views.confirmarContrasena,name='confirmarContra'),
    path(r'^montoDeposito/(?P<cedula>\d+)(?P<numero>\d+)/$',views.depositar,name='montoDeposito'),
    path('transferir/',views.transferencia,name='transferencia'),
    path('buscarTransferenciaOrigen/',views.buscarTransferenciaOrigen,name='buscarTransferenciaOrigen'),
    path('obtenerUser/',views.obtenerUser,name='obtenerUser'),
    path('Comprobante/',views.comprobante,name='comprobante'),
    path('CSV/',views.CSV,name='csv'),
    path('csvGenerar/',views.generarCsv,name='generarCsv'),
    
    
]
