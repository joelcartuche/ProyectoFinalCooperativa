from django import forms
from app.modelo.models import Cliente
class FormularioCliente (forms.ModelForm):

    
    class Meta:
        model = Cliente
        fields= ["cedula","nombres","apellidos","genero","estadoCivil","fechaNacimiento","correo","telefono","celular","direccion"]
        widgets = { 
     'fechaNacimiento': forms.DateInput(format='%Y-%m-%d',attrs={'type':'date'}), 
    } 