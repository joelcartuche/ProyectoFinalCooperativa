from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioCliente
from app.modelo.models import Cliente

# Create your views here.
@login_required
def principal(request):
    return render(request,'principal/principal.html')


@login_required
def crear_cliente(request):
    formulario = FormularioCliente(request.POST)
    titulo = 'Creacion de datos'
    if request.method ==  'POST':
        if formulario.is_valid():
            cliente = Cliente()
            datos = formulario.cleaned_data
            cliente.cedula = datos.get('cedula')
            cliente.nombres = datos.get('nombres')
            cliente.apellidos= datos.get('apellidos')
            cliente.genero = datos.get('genero')
            cliente.estadoCivil = datos.get('estadoCivil')
            cliente.fechaNacimiento = datos.get('fechaNacimiento')
            cliente.correo = datos.get('correo')
            cliente.telefono = datos.get('telefono')
            cliente.celular = datos.get('celular')
            cliente.direccion= datos.get('direccion')
            cliente.save()
            return redirect('principal')
    return render(request,'clientes/crear_cliente.html',locals())
