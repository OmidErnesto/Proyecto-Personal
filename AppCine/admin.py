from django.contrib import admin

# Register your models here.
from.models import Pelicula,UsuarioCliente,Sala,Reserva,Promocion,Entrada,Cartelera

admin.site.register(Pelicula)
admin.site.register(UsuarioCliente)
admin.site.register(Sala)
admin.site.register(Reserva)
admin.site.register(Promocion)
admin.site.register(Entrada)
admin.site.register(Cartelera)