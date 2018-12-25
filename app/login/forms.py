from django import forms

class Formulario(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={'class':'form-username form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-password form-control'}))