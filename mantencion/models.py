from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Servicio(models.Model):
    Horaatencion=models.CharField(max_length=4)
    Fechaatencion=models.CharField(max_length=6)
    Horainicio=models.CharField(max_length=4)
    Horatermino=models.CharField(max_length=4)
    Idascensor=models.CharField(max_length=5)
    Modeloascensor=models.CharField(max_length=30)
    Falladetectada=models.CharField(max_length=100)
    Reparacionesefectuadas=models.CharField(max_length=100)
    Piezascambiadas=models.CharField(max_length=100)
    Recibetrabajo=models.CharField(max_length=100)

    def __str__(self):
        return self.Horaatencion

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=70)
    ciudad = models.CharField(max_length=30)
    comuna = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.nombre

class Orden(models.Model):
    folio = models.AutoField(primary_key=True)
    cliente = models.ForeignKey('Cliente',db_column='nombre', on_delete=models.CASCADE)
    fecha = models.DateField()
    horainicio = models.TimeField()
    horafin = models.TimeField()
    idascensor = models.IntegerField()
    modeloasc = models.CharField(max_length=30)
    fallas = models.CharField(max_length=200, blank=True, null=True)
    reparaciones = models.CharField(max_length=200, blank=True, null=True)
    piezascambiadas = models.CharField(max_length=100, blank=True, null=True)
    receptor = models.CharField(max_length=50)
    tecnico = models.ForeignKey('tecnico', on_delete=models.CASCADE)

class tecnico(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
