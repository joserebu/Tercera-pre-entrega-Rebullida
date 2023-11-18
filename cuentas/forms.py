from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class formulario_creacion(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}    
        
class formulario_edicion(UserChangeForm):
    password = None
    first_name = forms.CharField(label='Ingresar Nombre', required=False)
    last_name = forms.CharField(label='Ingresar Apellido', required=False)
    email = forms.EmailField(label='Cambiar email', required=False)
    biografia = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
        
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'biografia', 'avatar']
        help_texts = {key: '' for key in fields} 
    