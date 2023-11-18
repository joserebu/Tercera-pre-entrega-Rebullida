from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from inicio.models import Cocina, Televisor, Heladera
from inicio.forms import crear_cocina_formulario, crear_televisor_formulario, busqueda_cocina_formulario, editar_televisor_formulario


def inicio(request):
    return render(request, "inicio/inicio.html", {})

@login_required
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

@login_required
def crear_televisor(request):
    if request.method == 'POST':
        formulario = crear_televisor_formulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            modelo = info_limpia.get('modelo')
            tamano_pantalla = info_limpia.get('tamano_pantalla')
            descripcion = info_limpia.get('descripcion')
            precio = info_limpia.get('precio')            
                
            televisor = Televisor(marca=marca, modelo=modelo, tamano_pantalla=tamano_pantalla, descripcion=descripcion, precio=precio)
            televisor.save()
            
            return redirect('televisor')    
        else:
            return render (request, 'inicio/crear_televisor.html', {'formulario_tv': formulario})
    
    formulario = crear_televisor_formulario
    return render (request, 'inicio/crear_televisor.html', {'formulario_tv': formulario})

def televisor(request):
   
    busqueda_marca = request.GET.get('marca')
    
    if busqueda_marca:
        listado_televisor = Televisor.objects.filter(marca__icontains=busqueda_marca)
    else:
        listado_televisor = Televisor.objects.all()
    
    return render(request, 'inicio/televisores.html', {'listado_televisor': listado_televisor})

@login_required
def eliminar_televisor(request, televisor_id):
    televisor_a_eliminar = Televisor.objects.get(id=televisor_id)
    televisor_a_eliminar.delete()
    return redirect("televisor")

@login_required
def editar_televisor(request, televisor_id):
    televisor_a_editar = Televisor.objects.get(id=televisor_id)
    
    if request.method == 'POST':
        formulario = editar_televisor_formulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            televisor_a_editar.marca = info_limpia.get('marca')
            televisor_a_editar.modelo = info_limpia.get('modelo')
            televisor_a_editar.tamano_pantalla = info_limpia.get('tamano_pantalla')
            televisor_a_editar.descripcion = info_limpia.get('descripcion')
            televisor_a_editar.precio = info_limpia.get('precio')
            
            televisor_a_editar.save()
            return redirect('televisor')
        else:
            return render(request, 'inicio/editar_televisor.html', {'formulario': formulario})
            

    formulario = editar_televisor_formulario(initial={'marca': televisor_a_editar.marca, 'modelo': televisor_a_editar.modelo, 'tamano_pantalla': televisor_a_editar.tamano_pantalla, 'descripcion': televisor_a_editar.descripcion, 'precio': televisor_a_editar.precio})
    return render(request, 'inicio/editar_televisor.html', {'formulario_tv': formulario})

def detalle_televisor(request, televisor_id):
    televisor = Televisor.objects.get(id=televisor_id)
    
    return render(request, 'inicio/detalle_televisor.html', {'televisor': televisor})

def heladera(request):
   
    busqueda_marca = request.GET.get('marca')
    
    if busqueda_marca:
        listado_heladera = Heladera.objects.filter(marca__icontains=busqueda_marca)
    else:
        listado_heladera = Heladera.objects.all()
    
    return render(request, 'inicio/heladeras.html', {'listado_heladera': listado_heladera})


# Vistas basadas en clases

class ListadoHeladeras(ListView):
    model = Heladera
    context_object_name = 'listado_heladera'
    template_name = 'inicio/heladeras.html'


class CrearHeladera(LoginRequiredMixin, CreateView):
    model = Heladera
    template_name = "inicio/crear_heladera.html"
    fields = ['marca', 'modelo', 'descripcion', 'tipo_freezer','precio']
    success_url = reverse_lazy('heladera')


class EditarHeladera(LoginRequiredMixin, UpdateView):
    model = Heladera
    template_name = "inicio/editar_heladera.html"
    fields = ['marca', 'modelo', 'descripcion', 'tipo_freezer','precio']
    success_url = reverse_lazy('heladera')


class DetalleHeladera(DetailView):
    model = Heladera
    template_name = "inicio/detalle_heladera.html"


class EliminarHeladera(LoginRequiredMixin, DeleteView):
    model = Heladera
    template_name = "inicio/eliminar_heladera.html"
    success_url = reverse_lazy('heladera')