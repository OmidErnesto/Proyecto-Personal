from django.db import models
from django.urls import reverse

class Pelicula(models.Model):
    titulo = models.CharField(max_length=30,primary_key=True)
    gen = [
        ("Terror","Terror"),
        ("Drama","Drama"),
        ("Comedia","Comedia"),
        ("Accion","Accion"),
        ("Suspenso","Suspenso")
    ]
    genero = models.CharField(max_length=20,choices=gen)
    edad = models.BooleanField()   # Mayores o menores de 18
    idim = [
        ("Ingles","Ingles"),
        ("Español","Español"),
    ]
    idioma = models.CharField(max_length=20,choices=idim)
    #duracion =
    #sinopsis =  models.ForeignKey(Sinopsis, blank=False, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='pics')
    def __str__(self):
        texto = "{0}"
        return texto.format(self.titulo)

    def get_absolute_url(self):
        return reverse('AppCine:Peliculas', kwargs={'myID': self.id })

class UsuarioCliente (models.Model):
    IdCliente = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    edad = models.IntegerField()
    dni = models.CharField(max_length=8)
    correo = models.EmailField(max_length=50)
    #cliente

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombres)


class Sala(models.Model):
    idSala = models.CharField(max_length=3,primary_key=True)
    capacidad = models.IntegerField()

class Reserva(models.Model):
    #tipo de cliente
    #Pelicula = UsuarioCliente.pelicula
    hora = models.CharField(max_length=15)
    sala = models.ForeignKey(Sala,blank=False,on_delete=models.CASCADE)

class Promocion(models.Model):
    descuento = models.BooleanField()
    #tipo de cliente

class Entrada(models.Model):
    descripcion = models.TextField()
    precio = models.IntegerField()
    #fecha = models.TimeField
    IdCliente = models.CharField(max_length=10)
    promocion = models.BooleanField()

class Cartelera(models.Model):
    peliculas = []
    #Promocion = BooleanField()
    #sala = models.ForeingKey(Sala, blank=False, on_delete=models.CASCADE)
    #horario = models.TimeField