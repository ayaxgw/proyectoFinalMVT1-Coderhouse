from django.shortcuts import render
from tienda_electrodomesticos.models import * 

# Create your views here.

def vista_inicio(request):
    return render(request, "tienda_electrodomesticos/index.html")


