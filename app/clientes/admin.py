from django.contrib import admin
from app.modelo.models import Cliente,Banco,Cuenta,Transaccion

class AdminCliente(admin.ModelAdmin):

    list_display = ["estado","cedula", "nombres", "apellidos", "genero", "estadoCivil", "fechaNacimiento", "correo", "telefono", "celular", "direccion"]
    list_editable = ["apellidos", "nombres", "genero"]
    list_filter = ["estado","genero", "direccion", "fechaNacimiento", "estadoCivil"]
    search_fields = ["cedula", "nombres", "apellidos"]

    class Meta:
        model = Cliente

admin.site.register(Cliente, AdminCliente)

class AdminBanco(admin.ModelAdmin):
    list_display = ["nombre_Banco", "direccion_Banco", "telefono_Banco", "correo_Banco"]
    list_editable = ["direccion_Banco", "telefono_Banco", "correo_Banco"]
    list_filter = ["direccion_Banco"]
    search_fields = ["nombre_Banco", "correo_Banco"]

    class Meta:
        model = Banco

admin.site.register(Banco, AdminBanco)

class AdminCuenta(admin.ModelAdmin):

    list_display = ["numero", "fechaApertura", "saldo", "tipoCuenta", "cliente"]
    list_filter = ["fechaApertura", "tipoCuenta"]
    search_fields = ["numero", "cliente"]

    class Meta:
        model = Cuenta

admin.site.register(Cuenta, AdminCuenta)

class AdminTransaccion(admin.ModelAdmin):

    list_display = ["fecha", "tipo", "valor", "descripcion", "responsable", "cuenta"]
    list_filter = ["tipo", "responsable"]
    search_fields = ["cuenta", "descripcion"]

    class Meta:
        model = Transaccion

admin.site.register(Transaccion, AdminTransaccion)
