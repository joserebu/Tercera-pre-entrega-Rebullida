from django.urls import path
from django.contrib.auth.views import LogoutView
from cuentas.views import login, registro, editar_perfil, cambiar_password, detalle_usuario


urlpatterns = [
    path('login/', login, name = 'login'),
    path('logout/', LogoutView.as_view(template_name='cuentas/logout.html'), name = 'logout'),
    path('registro/', registro, name = 'registrarse'),
    path('perfil/detalle/', detalle_usuario.as_view(), name = 'detalle_usuario'),
    path('perfil/editar/', editar_perfil, name = 'editar_perfil'),
    path('perfil/editar/password', cambiar_password.as_view(), name = 'cambiar_password'),
]   
