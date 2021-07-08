from django.contrib import admin

# Register your models here.
from.models import UsuarioCliente,Pelicula,Sala, Reservas, Promocion, Entrada, Cartelera

admin.site.register(UsuarioCliente)
admin.site.register(Pelicula)
admin.site.register(Sala)
admin.site.register(Reservas)
admin.site.register(Promocion)
admin.site.register(Entrada)
admin.site.register(Cartelera)