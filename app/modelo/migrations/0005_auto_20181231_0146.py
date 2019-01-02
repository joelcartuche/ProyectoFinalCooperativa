# Generated by Django 2.1.4 on 2018-12-31 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0004_auto_20181226_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(choices=[('retiro', 'Retiro'), ('deposito', 'Depósito'), ('transferencia', 'Transferencia'), ('prestamo', 'Pago de Prestamo'), ('nomina', 'Pagos de Nómina'), ('pensiones', 'Pagos de Pensiones'), ('dividendos', 'Dividendos'), ('reembolsoGastos', 'Reembolso de Gastos'), ('pagoProveedores', 'Reembolso de Gastos'), ('transferenciaBancaria', 'Traslado de efectivo entre entidades bancarias'), ('seguros', 'Pago de Seguros'), ('iess', 'Pago del IESS'), ('hipotecas', 'Pago de Hipotecas'), ('serviciosBasico', 'Pago de Servicios Básicos'), ('tvCable', 'Cuentas de televisión por cable'), ('celular', 'Cuentas de celular'), ('online', 'Compras por Internet'), ('administracion', 'Servicio de Administración'), ('futuros', 'Pagos Futuros')], max_length=30),
        ),
    ]
