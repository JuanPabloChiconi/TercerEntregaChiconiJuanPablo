from django import forms

"""
class CursoFormulario(forms.Form):

    #Especificar los campos
    curso = forms.CharField()
    camada = forms.IntegerField()


class ProfesorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=30)
    
"""


class SensoresFormulario(forms.Form):   
    identificacion= forms.CharField(max_length=30)
    modelo= forms.CharField(max_length=30)
    valor= forms.CharField(max_length=30)

class DatosPersonalesFormulario(forms.Form):   
    direccion= forms.CharField(max_length=30)
    telefono= forms.CharField(max_length=30)
    email= forms.EmailField()

class UsuarioFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    dni= forms.CharField(max_length=30)
    