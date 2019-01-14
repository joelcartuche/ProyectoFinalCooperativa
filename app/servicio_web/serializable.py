from rest_framework import routers, serializers, viewsets
from app.modelo.models import Cliente,Cuenta,Transaccion
from rest_framework.views import APIView


class clienteSerializable(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields= ("estado","cedula","nombres","apellidos","genero","estadoCivil","fechaNacimiento","correo","telefono","celular","direccion")

class cuentaSerializable(serializers.ModelSerializer):
    class Meta:
        model= Cuenta
        fields= ("numero","fechaApertura","saldo","tipoCuenta")


class transaccionSerializable(serializers.ModelSerializer):
    class Meta:
        model= Transaccion
        fields= ("fecha","tipo","valor","descripcion","responsable")