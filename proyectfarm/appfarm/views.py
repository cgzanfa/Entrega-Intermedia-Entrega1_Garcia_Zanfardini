from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from appfarm.forms import *
from appfarm.models import *

# Create your views here.
def inicio(request):
    return render(request, "appfarm/base.html")

def creacion_clientes(request):

    if request.method == "POST":
        formulario = ClienteFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            cliente = Cliente(nombre=data["nombre"], apellido=data["apellido"], email=data["email"], nro_cliente=data["nro_cliente"])

            cliente.save()

    formulario = ClienteFormulario()
    contexto = {"formulario": formulario}
    return render(request, "appfarm/clientes_formulario.html", contexto)



def creacion_frutas(request):

    if request.method == "POST":
        formulario = FrutaFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            fruta = Fruta(fruta=data["fruta"], precio=data["precio"], nro_articulo=data["nro_articulo"])

            fruta.save()

    formulario = FrutaFormulario()
    contexto = {"formulario": formulario}
    return render(request, "appfarm/fruta_formulario.html", contexto)



def creacion_vegetales(request):

    if request.method == "POST":
        formulario = VegetalFormulario(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            vegetal = Vegetal(vegetal=data["vegetal"], precio=data["precio"], nro_articulo=data["nro_articulo"])

            vegetal.save()

    formulario = VegetalFormulario()
    contexto = {"formulario": formulario}
    return render(request, "appfarm/vegetal_formulario.html", contexto)



def buscar_vegetal(request):

    return render(request, "appfarm/busqueda_vegetal.html")



def resultado_busqueda_vegetal(request):

    nombre_vegetal = request.GET["nombre_vegetal"] 
            
    vegetales = Vegetal.objects.filter(vegetal__icontains=nombre_vegetal)

    return render(request, "appfarm/resultado_busqueda_vegetal.html", {"vegetales": vegetales})
