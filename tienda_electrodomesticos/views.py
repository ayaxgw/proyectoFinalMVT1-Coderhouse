from django.shortcuts import render
from tienda_electrodomesticos.models import * 
from django.http import HttpResponse
from tienda_electrodomesticos.forms import *

# Create your views here.

def vista_inicio(request):
    return render(request, "tienda_electrodomesticos/inicio.html")

def vista_registro(request):
    if request.method == "POST":
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            user = Usuario(nombre = data["nombre"], apellido = data["apellido"], edad = data["edad"], email = data["email"], nombre_usuario = data["nombre_usuario"], contrasenia = data["clave"])
            user.save()
    formulario = UsuarioForm()
    return render(request, "tienda_electrodomesticos/registro.html", {"formulario": formulario})

def vista_producto(request):
    if request.method == "POST":
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            producto = Producto(nombre_producto = data["nombre_producto"], precio = data["precio"], observaciones = data["observaciones"])
            producto.save()
    formulario = ProductoForm()
    return render(request, "tienda_electrodomesticos/producto.html", {"formulario": formulario})

def vista_garantia(request):
    if request.method == "POST":
        formulario = GarantiaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            garantia = Garantia(tipo_reparacion = data["tipo_reparacion"],precio = data["precio"])
            garantia.save()
    formulario = GarantiaForm()
    return render(request, "tienda_electrodomesticos/garantia.html", {"formulario": formulario})    

def vista_inicio_sesion(request):
     return render(request, "tienda_electrodomesticos/iniciar_sesion.html")

def vista_busqueda(request):
    return render(request, "tienda_electrodomesticos/busqueda.html")

def vista_resultado(request):
    nombre_producto = request.GET["nombre_producto"]
    producto = Producto.objects.filter(nombre_producto__icontains=nombre_producto)
    return render(request, "tienda_electrodomesticos/resultados_busqueda.html", {"producto": producto})
