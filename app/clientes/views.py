from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioCliente,FormularioCuenta
from app.modelo.models import Cliente,Cuenta

# Create your views here.

@login_required
def crear_cliente(request):
    formulario = FormularioCliente(request.POST)
    formularioCuenta = FormularioCuenta(request.POST)
    titulo = 'Creacion de datos'
    if request.method ==  'POST':
        if formulario.is_valid() and formularioCuenta.is_valid():
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

            datosCuenta = formularioCuenta.cleaned_data
            cuenta= Cuenta()
            cuenta.numero = datosCuenta.get('numero')
            cuenta.saldo = datosCuenta.get('saldo')
            cuenta.tipoCuenta = datosCuenta.get('tipoCuenta')
            cuenta.cliente = cliente
            
            cuenta.save()
            return redirect('principal')
    return render(request,'clientes/crear_cliente.html',locals())


@login_required
def principal(request):
        usuario = request.user
        if usuario.has_perm('modelo.add_cliente'):
                listaClientes = Cliente.objects.all().filter(estado=True).order_by('apellidos')
                context = {
                        'lista':listaClientes
                }

                return render(request,'clientes/listar_clientes_principal.html',context)

        else:
                return render(request,'clientes/acceso_prohibido.html')

@login_required
def gestion_clientes(request):
        usuario = request.user
        if usuario.has_perm('modelo.add_cliente'):
                listaClientes = Cliente.objects.all().order_by('apellidos')
                context = {
                        'lista':listaClientes
                }

                return render(request,'clientes/gestion_clientes.html',context)

        else:
                return render(request,'clientes/acceso_prohibido.html')


@login_required
def modificar(request,pk):
        client = Cliente.objects.get(cedula = pk)
        formulario = FormularioCliente(request.POST)
        if request.method == 'POST':
                formulario = FormularioCliente(request.POST)
                formulario.is_valid()
                datos = formulario.cleaned_data
                client.nombres = datos.get('nombres')
                client.apellidos= datos.get('apellidos')
                client.genero = datos.get('genero')
                client.estadoCivil =datos.get('estadoCivil')
                client.fechaNacimiento = datos.get('fechaNacimiento')
                client.telefono=datos.get('telefono')
                client.celular=datos.get('celular')
                client.direccion=datos.get('direccion')
                client.save()
                return redirect(principal)
        else:
                formulario = FormularioCliente(instance = client)
                context = {
                        'formulario':formulario
                }
        return render(request,'clientes/editar_cliente.html',context)


@login_required
def eliminar(request,pk):
    client = Cliente.objects.get(cedula = pk)
    if client:
            client.estado = False
            client.save()
            return redirect('principal')
    return render (request,'eliminar_cliente.html')