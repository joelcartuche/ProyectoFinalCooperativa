from django.db import models

# Create your models here.
class Cliente(models.Model):

    listaGenero = (
        ('f', 'Femenino'),
        ('m', 'Masculino'),
    )

    listaEstado=(
        ('s','soltero'),
        ('c','casado'),
        ('v','viudo'),
        ('d','divorsiado'),
    )

    cliente_id = models.AutoField(primary_key=True)
    cedula = models.CharField(unique=True, max_length=10, null = False)
    nombres = models.CharField(max_length=70, null = False)
    apellidos = models.CharField(max_length=70, null = False)
    genero = models.CharField(max_length=15, choices = listaGenero, null = False)
    estadoCivil = models.CharField(max_length=15, choices = listaEstado,null = False)
    fechaNacimiento = models.DateField(auto_now = False, auto_now_add = False, null = False)
    correo = models.EmailField(unique=True, max_length=100, null = False)
    telefono = models.CharField(max_length=15, null = False)
    celular = models.CharField(max_length=15, null = False)
    direccion = models.TextField(null = False)

    def __str__(self):
        return self.cedula

class Banco(models.Model):

    nombre_Banco = models.CharField(primary_key=True, max_length=25)
    direccion_Banco = models.CharField(max_length=225)
    telefono_Banco = models.CharField(max_length=10)
    correo_Banco = models.EmailField(max_length=200)

class Cuenta(models.Model):

    listaTipo = (
        ('corriente', 'Corriente'),
        ('ahorros', 'Ahorro'),
        ('basica', 'Básica'),
        ('nomina', 'Nómina'),
        ('valores', 'Valores'),
        ('juvenil', 'Juvenil'),
        ('programado', 'Ahorro Programado'),
        ('euros', 'Ahorro en Euros'),
    )
    cuenta_id = models.AutoField(primary_key=True)
    numero = models.CharField(max_length=20, unique=True, null = False)
    estado = models.BooleanField(null = False, default = True)
    fechaApertura = models.DateField(auto_now_add = True, null = False)
    saldo = models.DecimalField(max_digits=10, decimal_places=3, null = False)
    tipoCuenta = models.CharField(max_length=30, choices = listaTipo, null = False)
    cliente = models.ForeignKey(
        'Cliente',
        on_delete=models.CASCADE,
    )

class Transaccion(models.Model):

    listaTipoC = (
        ('retiro', 'Retiro'),
        ('deposito', 'Depósito'),
        ('transferencia', 'Transferencia'),
        ('prestamo', 'Pago de Prestamo'),
        ('nomina', 'Pagos de Nómina'),
        ('pensiones', 'Pagos de Pensiones'),
        ('dividendos', 'Dividendos'),
        ('reembolsoGastos', 'Reembolso de Gastos'),
        ('pagoProveedores', 'Reembolso de Gastos'),
        ('transferencia', 'Traslado de efectivo entre entidades bancarias'),
        ('seguros', 'Pago de Seguros'),
        ('iess', 'Pago del IESS'),
        ('hipotecas', 'Pago de Hipotecas'),
        ('serviciosBasico', 'Pago de Servicios Básicos'),
        ('tvCable', 'Cuentas de televisión por cable'),
        ('celular', 'Cuentas de celular'),
        ('online', 'Compras por Internet'),
        ('administracion', 'Servicio de Administración'),
        ('futuros', 'Pagos Futuros'),
    )
    transaccion_id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add = True, null = False)
    tipo = models.CharField(max_length=30, choices = listaTipoC, null = False)
    valor = models.DecimalField(max_digits=10, decimal_places=3, null = False)
    descripcion = models.TextField(null = False)
    responsable = models.CharField(max_length=160, null = False)
    cuenta = models.ForeignKey(
        'Cuenta',
        on_delete=models.CASCADE,
    )
