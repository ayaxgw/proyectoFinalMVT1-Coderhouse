from django import forms

class UsuarioForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    nombre_usuario = forms.CharField()
    clave = forms.CharField()

class ProductoForm(forms.Form):
    nombre_producto = forms.CharField()
    precio = forms.IntegerField()
    observaciones = forms.CharField()

class GarantiaForm(forms.Form):
    tipo_reparacion = forms.CharField()
    precio = forms.IntegerField()
       