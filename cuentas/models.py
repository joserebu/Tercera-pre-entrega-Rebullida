from django.db import models
from django.contrib.auth.models import User

class DatosExtra(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   biografia = models.CharField(max_length=300)
   avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
   

class DatosUsuario(models.Model):
    user = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.TextField()
    email = models.CharField
    biografia = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)