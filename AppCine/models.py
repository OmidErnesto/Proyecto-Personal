from django.db import models

# Create your models here.

#class Sinopsis(models.Model):
#    descripcion = models.TextField(primary_key=True)
#    calificacion = models.IntegerField()

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
    #sinopsis =  models.ForeignKey(Sinopsis, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.titulo)



class UsuarioCliente (models.Model):
    IdCliente = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    edad = models.IntegerField()
    pelicula = models.ForeignKey(Pelicula,blank=False,on_delete=models.CASCADE)
    dni = models.CharField(max_length=8)
    correo = models.EmailField(max_length=50)
    #cliente

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombres)


class Sala(models.Model):
    idSala = models.CharField(max_length=3,primary_key=True)
    capacidad = models.IntegerField()
    
class Reservas(models.Model):
    #tipo de cliente
    #Pelicula = UsuarioCliente.pelicula
    hora = models.CharField(max_length=8)
    sala = models.ForeignKey(Sala,blank=False,on_delete=models.CASCADE)

class Promocion(models.Model):
    descuento = models.BooleanField
    #tipo de cliente

class Entrada(models.Model):
    descripcion = models.TextField()
    precio = models.IntegerField()
    #fecha = models.TimeField
    IdCliente = models.CharField(max_length=10)
    Promocion = models.BooleanField

class Cartelera(models.Model):
    peliculas = []
    #Promocion = BooleanField
    #sala = models.ForeingKey(Sala, blank=False, on_delete=models.CASCADE)
    #horario = models.TimeField