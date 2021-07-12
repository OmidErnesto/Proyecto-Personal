from AppCine.models import Pelicula
from django import forms

class PeliculaForm(forms.Form):
    titulo = forms.CharField()
    gen = [
        ("Terror","Terror"),
        ("Drama","Drama"),
        ("Comedia","Comedia"),
        ("Accion","Accion"),
        ("Suspenso","Suspenso")
    ]
    genero = forms.ChoiceField(choices=gen)
    edad = forms.BooleanField(required=False)   # Mayores o menores de 18
    idim = [
        ("Ingles","Ingles"),
        ("Español","Español"),
    ]
    idioma = forms.ChoiceField(choices=idim)

class UsuarioForms(forms.Form):
    IdCliente = forms.IntegerField()
    nombres = forms.CharField()
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    dni = forms.CharField()
    correo = forms.EmailField()
