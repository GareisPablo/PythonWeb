from django.http import HttpResponse
from django.shortcuts import render
from Portafolio.models import Datos
# Create your views here.

def dato(seft):
    dato=Datos(nombrecompleto="Juan",edad=31,dni=22334432)
    dato.save()
    documentohtml=f"Datos Creados: {dato.nombrecompleto} {dato.edad} {dato.dni}"
    return HttpResponse(documentohtml)