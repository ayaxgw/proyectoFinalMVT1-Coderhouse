from django.urls import path
from tienda_electrodomesticos.views import *

urlpatterns = [
    path("inicio/", vista_inicio, name = "Comercio-inicio"),
    path("registro/", vista_registro, name = "Comercio-registro"),
    path("producto/", vista_producto, name = "Comercio-producto"),
    path("iniciar_sesion/", vista_inicio_sesion, name="Comercio-iniciar-sesion"),
    path("busqueda/", vista_busqueda, name="comercio-busqueda"),
    path("resultado_busqueda/", vista_resultado, name="comercio-busqueda-resultado")

]