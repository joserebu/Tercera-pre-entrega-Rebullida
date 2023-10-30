from django.db import models

class Cocina(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=30)
    descripcion = models.TextField()
    tipo_gas = models.TextField()