from django.shortcuts import render, redirect
from django.http import HttpResponse
from appfarm.forms import *
from appfarm.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from proyectfarm.settings import BASE_DIR
import os

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



def entregables(request):
    return render(request, "appfarm/entregables.html")



class EntregablesList(ListView):

    model = Entregable
    template_name = "appfarm/list_entregables.html"


class EntregableDetail(DetailView):

    model = Entregable
    template_name = "appfarm/detail_entregable.html"


class EntregableCreate(CreateView):

    model = Entregable
    succsess_url = "/farm/entregables/"
    fields = ["nombre", "fecha_de_entrega", "entregado"]
    template_name = "appfarm/entregable_form.html"


class EntregableUpdate(UpdateView):

    model = Entregable
    succsess_url = "/farm/entregables/"
    fields = ["fecha_de_entrega", "entregado"]


class EntregableDelete(DeleteView):

    model = Entregable
    success_url = "/farm/entregables/"





def entregables(request):
    return render(request, "appfarm/entregables.html")


def test(request):
    ruta = os.path.join(BASE_DIR, "appfarm/templates/appfarm/base.html")
    print(BASE_DIR, __file__)
    file = open(ruta)

    return HttpResponse(file.read())
