from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='autenticar'),
    path('logout/',views.salir,name='logout')
]