from rest_framework import routers, serializers, viewsets
from app.modelo.models import Cliente,Cuenta,Transaccion
from .serializable import clienteSerializable,cuentaSerializable,transaccionSerializable
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import *

class listaCliente(APIView):
    def get(self,request):
        owner = serializers.Field()
        lista = Cliente.objects.all()
        objetoSerializable = clienteSerializable(lista,many = True)
        return Response(objetoSerializable.data)

class listaCuenta(APIView):
    def get(self,request):
        owner = serializers.Field()
        lista = Cuenta.objects.all()
        objetoSerializable = cuentaSerializable(lista,many = True)
        return Response(objetoSerializable.data)

class listaTransaccion(APIView):
    def get(self,request):
        owner = serializers.Field()
        lista = Transaccion.objects.all()
        objetoSerializable = transaccionSerializable(lista,many = True)
        return Response(objetoSerializable.data)


class busquedaCliente(APIView):
    def get(self,request):
        ceduApellido = request.GET['cedula']
        if Cliente.objects.filter(cedula = ceduApellido):
            lista = Cliente.objects.filter(cedula = ceduApellido)
        
        objetoSerializable = clienteSerializable(lista,many = True)
        return Response(objetoSerializable.data)

class busquedaCuenta(APIView):
    def get(self,request):
        numeroCuenta = request.GET['numero']
        if Cuenta.objects.filter(numero = numeroCuenta):
            lista = Cuenta.objects.filter(numero = numeroCuenta)
        objetoSerializable = cuentaSerializable(lista,many = True)
        return Response(objetoSerializable.data)

class busquedaTransaccion(APIView):
    def get(self,request):
        numeroCuenta = request.GET['numero']
        if Transaccion.objects.filter(cuenta__numero = numeroCuenta):
            lista = Transaccion.objects.filter(cuenta__numero = numeroCuenta)
        objetoSerializable = transaccionSerializable(lista,many = True)
        return Response(objetoSerializable.data)

