from django.db import models

# Create your models here.

#creo la clase para la tabla en la base de datos

class Datos(models.Model):
    #string
    nombrecompleto=models.CharField(max_length=50)
    #int
    edad= models.IntegerField()
    dni= models.IntegerField()