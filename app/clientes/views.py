from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioCliente,FormularioCuenta,FormularioMonto,FormularioTransaccion
from app.modelo.models import Cliente,Cuenta,Transaccion
from django.http import HttpResponse
#importamos para generar pdf
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

import csv

from weasyprint import HTML, CSS
from django.template.loader import get_template,render_to_string
from django.http import HttpResponse
from weasyprint.fonts import FontConfiguration


# Create your views here.

@login_required
def crear_cliente(request):
        usuario = request.user
        if usuario.has_perm('modelo.add_cliente'):
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
        else:
                return render(request,'clientes/acceso_prohibido.html')


@login_required
def principal(request):
        usuario = request.user
        if usuario.has_perm('modelo.view_cliente'):
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
        if usuario.has_perm('modelo.view_cliente'):
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
    if request.method == 'POST':
            client.estado = False
            client.save()
            return redirect('gestion')
    else:
            return render (request,'clientes/confirmar.html')


@login_required
def activar(request,pk):
    client = Cliente.objects.get(cedula = pk)
    if client:
            client.estado = True
            client.save()
            return redirect('gestion')




@login_required
def buscar(request,pk,pk2):
        if pk:
                listaClientes1 = Cliente.objects.all().filter(cedula=pk).order_by('apellidos')
        if pk2:
                listaClientes2 = Cliente.objects.all().filter(cedula=pk2).order_by('apellidos')
        return render(request,'clientes/editar_cliente.html',locals())



@login_required
def listarClienteCuenta(request):
        lista= Cliente.objects.all().filter().values('cedula','nombres','apellidos','correo','cuenta__numero',
        'cuenta__saldo','cuenta__tipoCuenta').order_by('apellidos')
        return render(request,'clientes/transacciones/deposito.html',locals())

@login_required
def listarClienteCuentaBusqueda(request):
        cedula = request.GET['cedula']
        lista= Cliente.objects.all().filter(cedula=cedula).values('cedula','nombres','apellidos','correo','cuenta__numero',
        'cuenta__saldo','cuenta__tipoCuenta').order_by('apellidos')
        return render(request,'clientes/transacciones/deposito.html',locals())

@login_required
def confirmarContrasena(request):
        confirmar = False
        contra = request.GET['contra']
        if request.user.check_password(contra):
                confirmar=True
        return HttpResponse(confirmar)

@login_required
def depositar(request,cedula,numero):
        formulario = FormularioMonto(request.POST)
        formularioTransaccion= FormularioTransaccion(request.POST)       
        cliente=Cliente.objects.all().filter(cedula = cedula)
        cuenta = Cuenta.objects.all().filter(numero = numero)
        if request.method == 'POST':
                if formulario.is_valid() and formularioTransaccion.is_valid():
                        datos = formulario.cleaned_data
                        datosTransaccion = formularioTransaccion.cleaned_data
                        transaccion = Transaccion()
                        deposito = float(datosTransaccion.get('valor'))
                        aux=str(Cuenta.objects.get(numero = numero))
                        aux = aux.split(';')
                        saldoActual = float(aux[0])
                        transaccion.tipo= datosTransaccion.get('tipo')
                        transaccion.valor = datosTransaccion.get('valor')
                        transaccion.descripcion = datosTransaccion.get('descripcion')
                        transaccion.responsable = datosTransaccion.get('responsable')
                        transaccion.cuenta = Cuenta.objects.get(cuenta_id=int(aux[1]))
                        

                        if datosTransaccion.get('tipo') =='deposito':
                                transaccion.save()
                                for cu in cuenta:
                                        cu.saldo =round(saldoActual+deposito,3)
                                        cu.save()
                                #datos a recogerse en el template
                                titulo='Transacción'
                                subtitulo='Depósito'
                                mensaje='Deposito realizado con éxito'
                                valor=True
                                numero1 = numero
                                cedula1 = cedula
                                monto = datosTransaccion.get('valor')

                                return render (request,'clientes/mensajes/estado.html',locals())
                        if datosTransaccion.get('tipo') =='retiro':
                                transaccion.save()
                                for cu in cuenta:
                                        cu.saldo =round(saldoActual-deposito,3)
                                        cu.save()
                                #datos a recogerse en el template
                                titulo='Transacción'
                                subtitulo='Retiro'
                                mensaje='Retirorealizado con éxito'
                                valor=True
                                numero1 = numero
                                cedula1 = cedula
                                monto = datosTransaccion.get('valor')         
                                return render (request,'clientes/mensajes/estado.html',locals())

        else:
                return render (request,'clientes/transacciones/monto_deposito.html',locals())





@login_required
def transferenciaLista(request):
        return render (request,'clientes/transferencia_cliente.html')


@login_required
def buscarTransferenciaOrigen(request):
        confirmar = False
        numero = request.GET['numero']
        lista= Cliente.objects.all().filter(cuenta__numero=numero).values('cedula','nombres','apellidos','correo','cuenta__numero',
        'cuenta__saldo','cuenta__tipoCuenta').order_by('apellidos')
        listaCuenta= Cuenta.objects.all().filter(numero=numero).values('numero',
        'saldo','tipoCuenta')
        data = ''
        for i in lista.values():
                data =i['cedula']+";"+i['nombres']+";"+i['apellidos']+";"+i['correo']+";"
        
        for i in listaCuenta.values():
                data += i['numero']+";"+str(i['saldo'])+";"+i['tipoCuenta']

        return HttpResponse(data)


@login_required
def obtenerUser(request):
        user = request.user.username
        return HttpResponse (user)


@login_required
def transferencia(request):
        numero1 = request.GET['numero1']
        cedula1= request.GET['cedula1']
        numero2 = request.GET['numero2']
        cedula2 = request.GET['cedula2']
        valor = request.GET['valor']
        descripcion = request.GET['descripcion']
        responsable = request.GET['responsable']

        cliente1=Cliente.objects.all().filter(cedula = cedula1)
        cuenta1 = Cuenta.objects.all().filter(numero = numero1)

        cliente2=Cliente.objects.all().filter(cedula = cedula2)
        cuenta2 = Cuenta.objects.all().filter(numero = numero2)

        titulo ="Transaccion"
        subtitulo ="transferencia"

        if cliente1 and cuenta1 and cliente2 and cuenta2:
                transaccion = Transaccion()

                auxCuenta1=str(Cuenta.objects.get(numero = numero1))
                auxCuenta2=str(Cuenta.objects.get(numero = numero2))

                auxCuenta1 =  auxCuenta1.split(';')
                auxCuenta2 =  auxCuenta2.split(';')

                saldoActual1 = float(auxCuenta1[0])
                saldoActual2 = float(auxCuenta2[0])

                transaccion.tipo= 'transferencia'
                transaccion.valor = round(float(valor),3)
                transaccion.descripcion = descripcion
                transaccion.responsable = responsable
                transaccion.cuenta = Cuenta.objects.get(cuenta_id=int(auxCuenta1[1]))

                deposito = float(valor)
               
                for cu in cuenta1:
                        cu.saldo =round(saldoActual1-deposito,3)
                        cu.save()
                
                transaccion.save()

                for cu in cuenta2:
                        cu.saldo =round(saldoActual2+deposito,3)
                        cu.save()
                mensaje ='Transacción realizada con éxito'
                valor = True
                monto =request.GET['valor']
                return render (request,'clientes/mensajes/estado.html',locals())
        else:
                valor = False
                mensaje ='ERROR AL REALIZAR TRANSACCION'
                return render (request,'clientes/mensajes/estado.html',locals())




@login_required
def comprobante( request):
        numero1 = request.GET['numero1']
        cedula1= request.GET['cedula1']
        numero2 = request.GET['numero2']
        cedula2 = request.GET['cedula2']
        valor = request.GET['valor']
        tipo =request.GET['tipo']

        font_config = FontConfiguration()
        listaCliente1= Cliente.objects.all().filter(cedula = cedula1 ).values('nombres','apellidos')
        listaCuenta1 = Cuenta.objects.all().filter(numero = numero1).values('tipoCuenta')

        listaCliente2= Cliente.objects.all().filter(cedula = cedula1 ).values('nombres','apellidos')
        listaCuenta2 = Cuenta.objects.all().filter(numero = numero1).values('tipoCuenta')

        html_template = render_to_string('./../template/pdf/comprobante.html',locals())
        response = HttpResponse(content_type='application/pdf')

        pdf_file = HTML(string=html_template).write_pdf()
        response = HttpResponse(pdf_file, content_type='application/pdf')

        response['Content-Disposition'] = 'filename="home_page.pdf"'

        return response

        