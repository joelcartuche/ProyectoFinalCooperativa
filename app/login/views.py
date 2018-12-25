from django.shortcuts import render
from .forms import Formulario

from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse



def loginPage(request):
    if request.method == 'POST':
        formulario = Formulario(request.POST)
        if formulario.is_valid():
            usuario = request.POST['username']
            clave = request.POST['password']
            user = authenticate(username = usuario, password = clave)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect(reverse('principal'))
                else:
                    messages.warning(request, 'Usuario inactivo')
            else:
                messages.warning(request, 'Usuario y/o contraseña')
            
    formulario = Formulario(request.POST)
    context = {
        'f': formulario
    }
    return render(request,'login/login.html',context)

def salir(request):
    logout(request)
    return HttpResponseRedirect(reverse('principal'))
 