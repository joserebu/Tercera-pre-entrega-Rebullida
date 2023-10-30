from django.urls import path
from inicio.views import inicio, cocina

urlpatterns = [
    path ('', inicio),
    path ('cocina/', cocina),
]
