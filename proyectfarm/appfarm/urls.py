from django.urls import path
from appfarm.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clientes/crear/", creacion_clientes, name="farm-clientes-crear"),
    path("fruta/crear/", creacion_frutas, name="farm-fruta-crear"),
    path("vegetal/crear/", creacion_vegetales, name="farm-vegetal-crear"),
    path("vegetal/buscar/", buscar_vegetal, name="farm-vegetal-buscar"),
    path("vegetal/buscar/resultado", resultado_busqueda_vegetal, name="farm-vegetal-buscar-resultado"),
    path("entregables/", EntregablesList.as_view(), name="farm-entregables"),
    path("entregables/detalle/<pk>/", EntregableDetail.as_view(), name="farm-entregables-detail"),
    path("entregables/crear/", EntregableCreate.as_view(), name="farm-entregables-create"),
    path("entregables/actualizar/<pk>/", EntregableUpdate.as_view(), name="farm-entregables-update"),
    path("entregables/borrar/<pk>/", EntregableDelete.as_view(), name="farm-entregables-delete"),
]