from django.urls import path
from inicio.views import inicio, cocina, televisor, crear_cocina, crear_televisor, eliminar_televisor, editar_televisor, detalle_televisor
from inicio.views import ListadoHeladeras, CrearHeladera, EditarHeladera, DetalleHeladera, EliminarHeladera

urlpatterns = [
    path ('', inicio, name='inicio'),    
    path ('cocina/', cocina, name='cocina'),
    path ('cocina/crear/', crear_cocina, name='crear_cocina'),
    path ('heladera/', ListadoHeladeras.as_view(), name='heladera'),
    path ('heladera/crear/', CrearHeladera.as_view(), name='crear_heladera'),
    path ('heladera/<int:pk>/editar/', EditarHeladera.as_view(), name='editar_heladera'),
    path ('heladera/<int:pk>/eliminar/', EliminarHeladera.as_view(), name='eliminar_heladera'),
    path ('heladera/<int:pk>/detalle/', DetalleHeladera.as_view(), name='detalle_heladera'),
    path ('televisor/', televisor, name='televisor'),
    path ('televisor/crear/', crear_televisor, name='crear_televisor'),
    path ('televisor/<int:televisor_id>/eliminar/', eliminar_televisor, name='eliminar_televisor'),
    path ('televisor/<int:televisor_id>/editar/', editar_televisor, name='editar_televisor'),
    path ('televisor/<int:televisor_id>/detalle/', detalle_televisor, name='detalle_televisor'),
]
