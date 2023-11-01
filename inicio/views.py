from django.shortcuts import render, redirect
from inicio.models import Cocina, Heladera, Televisor
from inicio.forms import crear_cocina_formulario, crear_heladera_formulario, crear_televisor_formulario, busqueda_cocina_formulario

def inicio(request):
    return render(request, "inicio/inicio.html", {})

def crear_cocina(request):
    if request.method == 'POST':
        formulario = crear_cocina_formulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            tipo_gas = info_limpia.get('tipo_gas')
            descripcion = info_limpia.get('descripcion')
            precio = info_limpia.get('precio')            
                
            cocina = Cocina(marca=marca, modelo=modelo, tipo_gas=tipo_gas, descripcion=descripcion, precio=precio)
            cocina.save()
            
            return redirect('cocina')    
        else:
            return render (request, 'inicio/crear_cocina.html', {'formulario': formulario})
    
    formulario = crear_cocina_formulario
    return render (request, 'inicio/crear_cocina.html', {'formulario': formulario})

def cocina(request):
    
    busqueda_marca = request.GET.get('marca')
    
    if busqueda_marca:
        listado_cocina = Cocina.objects.filter(marca__icontains=busqueda_marca)
    else:
        listado_cocina = Cocina.objects.all()
    
    return render(request, 'inicio/cocinas.html', {'listado_cocina': listado_cocina})

def heladera(request):
    heladera = Heladera(marca = 'Candy', modelo = 'Luxury', descripcion = 'heladera doble puerta', tipo_freezer = 'no frost', precio = 500000)
    heladera.save()
    
    return render(request, 'inicio/heladeras.html', {'heladera': heladera})

def televisor(request):
    televisor = Televisor(marca = 'Sony', modelo = 'DEX55M1900', tamano_pantalla = '55 pulgadas', descripcion = 'Televisro Led 4K colorTrue', precio = 500000)
    televisor.save()
    
    return render(request, 'inicio/televisores.html', {'televisor': televisor})

