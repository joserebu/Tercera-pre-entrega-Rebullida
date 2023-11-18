from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from cuentas.forms import formulario_creacion, formulario_edicion
from cuentas.models import DatosExtra, DatosUsuario

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('inicio')                      
       
    return render(request, 'cuentas/login.html', {'formulario_ingreso': formulario})


def registro(request):
    
    formulario = formulario_creacion()
    
    if request.method == 'POST':
        formulario = formulario_creacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
        
    return render(request, 'cuentas/registro.html',{'formulario_registro': formulario})


def editar_perfil(request):
    
    datos_extra = request.user.datosextra
    
    formulario = formulario_edicion(initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar},instance=request.user)

    if request.method == 'POST':
        formulario = formulario_edicion(request.POST, request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nuevo_avatar = formulario.cleaned_data.get('avatar')   
                    
            if nueva_biografia:
                datos_extra.biografia = nueva_biografia
            if nuevo_avatar:
                datos_extra.avatar = nuevo_avatar   
            
            datos_extra.save()
            formulario.save()
            
            return redirect('detalle_usuario')                   
    
    return render(request, 'cuentas/edicion.html', {'formulario_edicion': formulario})


class cambiar_password(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy("editar_perfil")
    
    
class detalle_usuario(PasswordChangeView):
    model = DatosUsuario
    template_name = "cuentas/descripcion.html"