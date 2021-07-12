"""Cine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from AppCine.views import CrearUsuario, PeliculaView, login, logout, myHome, registro, verPelicula
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', myHome, name='Pagina de Inicio'),
    path('admin/', admin.site.urls),
    path('peliculas', include('AppCine.urls')),
    path('crearPeliculas', PeliculaView,name="CrearPelicula"),
    path('peliculas/<str:myTitle>/',  verPelicula, name="VerPelicula"),
    path('crearUsuario', CrearUsuario,name="CrearUsuario"),
    path('registro/', registro,name="RegistroUsuario"),
    path('login/', login,name="LoginUsuario"),
    path('logout/', logout,name="Logout"),
]
