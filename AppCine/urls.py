from django.urls import path
from AppCine.views import login, myHome,PeliculaView, registro

urlpatterns = [
    path('/', myHome, name='Peliculas'),
    path('crearPeliculas/', PeliculaView, name='crearPeliculas'),
    path('registro/', registro,name="RegistroUsuario"),
    path('login/', login,name="LoginUsuario"),
]