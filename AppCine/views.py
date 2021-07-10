from django.shortcuts import render
from .models import Pelicula

# Create your views here.

def myHome(request, *args, **kwargs):

    peliculas = Pelicula.objects.all()
    print(args,kwargs)
    print(request.user)
    return render(request, "home.html", {'peliculas': peliculas})