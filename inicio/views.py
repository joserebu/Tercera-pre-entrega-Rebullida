from django.shortcuts import render
from inicio.models import Cocina

def inicio(request):
    return render(request, "inicio/inicio.html", {})

def cocina(request):
    cocina = Cocina(marca = 'Longvie', modelo = 'Premium', descripcion = 'cocina de 4 hornallas de 56cm', tipo_gas = 'envasado o natural')
    cocina.save()
    
    return render(request, 'inicio/cocinas.html', {'cocina': cocina})