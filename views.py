from cgitb import html
from django.shortcuts import render, HttpResponse

def home(request):

    return render(request, "home.html")

def Servicios(request):

    return render(request, "Servicios.html")

def Tienda(request):

    return render(request, "Tienda.html")

def Blog(request):

    return render(request, "Blog.html")

def Contacto(request):

    return render(request, "Contacto.html")