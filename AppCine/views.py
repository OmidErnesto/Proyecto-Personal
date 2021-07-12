from AppCine.forms import PeliculaForm, UsuarioForms
from django.shortcuts import redirect, render
from .models import Pelicula, UsuarioCliente
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def myHome(request, *args, **kwargs):

    peliculas = Pelicula.objects.all()
    print(args,kwargs)
    print(request.user)
    return render(request, "home.html", {'peliculas': peliculas})

def PeliculaView(request):
    form = PeliculaForm()
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Pelicula.objects.create(**form.cleaned_data)
            return redirect('/')
        else:
            print(form.errors)

    context = {
        'form':form,
    }
    
    return render(request, 'crearPelicula.html', context)

def verPelicula(request, myTitle):
    obj = Pelicula.objects.get(titulo = myTitle)
    context = {
        'objeto': obj
    }
    return render(request, 'descripcion.html', context)

def CrearUsuario(request):
    form = UsuarioForms()
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            UsuarioCliente.objects.create(**form.cleaned_data)
        else:
            print(form.errors)

    context = {
        'form':form,
    }
    
    return render(request, 'crearUsuario.html', context)

def registro(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'El Usuario ya existe')
                return redirect('registro')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Este email ya tiene una cuenta registrada')
                return redirect('registro')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('Usuario creado')
                return redirect('login')
        else:
            messages.info(request,'Las contraseñas no coinciden')
            return redirect('registro')
        return redirect('/')
    else:
        return render(request,'registro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Datos invalidos')
            return redirect('login')

    else:
         return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')