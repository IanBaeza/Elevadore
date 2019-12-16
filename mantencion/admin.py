from django.contrib import admin

# Register your models here.
from . models import Servicio,Cliente,Orden,tecnico

admin.site.register(Cliente)

admin.site.register(Orden)

admin.site.register(tecnico)