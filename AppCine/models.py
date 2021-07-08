from django.db import models

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=30,primary_key=True)
    gen = [
        ("T","Terror"),
        ("D","Drama"),
        ("C","Comedia"),
        ("A","Accion"),
        ("S","Suspenso")
    ]
    genero = models.CharField(max_length=1,choices=gen)
    edad = models.BooleanField   # Mayores o menores de 18
    idim = [
        ("I","Ingles"),
        ("E","Español"),
    ]
    idioma = models.CharField(max_length=1,choices=idim)
    #duracion =
    #sinopsis =  

    def __str__(self):
        texto = "{0}"
        return texto.format(self.titulo)

class UsuarioCliente (models.Model):
    IdCliente = models.IntegerField
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    edad = models.IntegerField
    pelicula = models.ForeignKey(Pelicula,blank=False,on_delete=models.CASCADE)
    dni = models.CharField(max_length=8)
    correo = models.EmailField(max_length=20)
    #cliente

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombres)


