from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    nombre_usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=30)
    precio = models.IntegerField()
    observaciones = models.CharField(max_length = 600)

class Garantia(models.Model):
    tipo_reparacion = models.CharField(max_length = 30)
    precio = models.IntegerField() 

# Realizando cambios en models.py para crear las migraciones