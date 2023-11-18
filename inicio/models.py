from django.db import models

class Cocina(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    tipo_gas = models.CharField(max_length=40)
    descripcion = models.TextField()
    precio = models.IntegerField()
        
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.precio}'

class Heladera(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField()
    tipo_freezer = models.CharField(max_length=40)    
    precio = models.IntegerField()
        
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.precio}'
    
class Televisor(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    tamano_pantalla = models.CharField(max_length=40)
    descripcion = models.TextField()
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.id} - {self.marca} - {self.modelo} - {self.precio}'
    