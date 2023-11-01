from django.urls import path
from inicio.views import inicio, cocina, heladera, televisor, crear_cocina

urlpatterns = [
    path ('', inicio, name='inicio'),
    path ('cocina/crear/', crear_cocina, name='crear_cocina'),
    path ('cocina/', cocina, name='cocina'),
    path ('heladera/', heladera, name='heladera'),
    path ('televisor/', televisor, name='televisor'),
]
