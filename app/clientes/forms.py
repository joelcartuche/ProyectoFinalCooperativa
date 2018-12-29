from django import forms
from app.modelo.models import Cliente,Cuenta,Transaccion
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

class FormularioMonto(forms.Form):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-password form-control','required':'true'}))

class FormularioTransaccion(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields=["tipo","valor","descripcion","responsable"]