from django.db import models
import uuid
# Create your models here.
class Reserva(models.Model):
    id = models.AutoField(primary_key = True,)
    nombre = models.CharField(max_length=40, null=False )
    apellido = models.CharField(max_length=40, null=False)
    telefono = models.IntegerField(null=False)
    fecha = models.DateField( )
    hora = models.TimeField( )
    cantidadPersonas = models.IntegerField(null=False)
    estado = models.CharField(max_length=40, null=False)
    observacion = models.CharField(max_length=500, null=True)

    