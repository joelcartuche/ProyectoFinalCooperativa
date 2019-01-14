from django import forms

class Formulario(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput())