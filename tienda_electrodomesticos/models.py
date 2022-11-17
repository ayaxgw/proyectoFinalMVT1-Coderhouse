from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    nombre_usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)

class Electrodomestico(models.Model):
    tipo_electrodomestico = models.CharField(max_length=30)
    precio = models.IntegerField()
    especificaciones = models.CharField(max_length = 200)

class Garantia(models.Model):
    tipo_reparacion = models.CharField(max_length = 30)
    precio = models.IntegerField() 