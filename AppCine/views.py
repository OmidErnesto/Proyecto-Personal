from django.shortcuts import render

# Create your views here.

def myHome(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    return render(request, "home.html", {})