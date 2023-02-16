from django.db import models

class EstadosDelCamion(models.TextChoices):
    DISPONIBLE = 'Disponible'
    VIAJE = 'Viajando'
    REPARACIONES = 'Reparaciones'

class Camion(models.Model):
    capacidad = models.DecimalField(decimal_places=2, max_digits=6)
    marca = models.CharField(max_length=10)
    modelo = models.CharField(max_length=4)
    placa = models.CharField(max_length=8)
    estado = models.CharField(
        max_length=12,
        choices=EstadosDelCamion.choices,
        default=EstadosDelCamion.DISPONIBLE
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Conductor(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

class Viaje(models.Model):
    origen = models.DateTimeField(auto_now_add=True)
    destino = models.DateTimeField(auto_now_add=True)

class Gastos(models.Model):
    combustible = models.DecimalField(decimal_places=2, max_digits=5)
    viaticos = models.DecimalField(decimal_places=2, max_digits=5)
    peajes= models.DecimalField(decimal_places=2, max_digits=5)