from django import forms
from app.modelo.models import Cliente,Cuenta
class FormularioCliente (forms.ModelForm):
    class Meta:
        model = Cliente
        fields= ["cedula","nombres","apellidos","genero","estadoCivil","fechaNacimiento","correo","telefono","celular","direccion"]
        widgets = { 
        'fechaNacimiento': forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'}), 
         } 

class FormularioCuenta(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields=["numero","saldo","tipoCuenta"]

