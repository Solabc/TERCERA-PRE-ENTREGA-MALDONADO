from django.shortcuts import render

from django.http import HttpResponse

from .models import Grado

# Create your views here.

def crear_grado(request):
    año = input("Ingrese el año: ")
    seccion = input("ingrese la seccion: ")
    
    grado = Grado(año=año, seccion=seccion)
    grado.save()
    texto = f"Registro exitoso"
    
    return HttpResponse(texto)

def mostrar_grados(request):
    
    grado = Grado.objects.all()
    
    contexto ={"grado": Grado}
    
    return render (request,"grado.html",contexto)