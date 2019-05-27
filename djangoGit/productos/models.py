# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class DatosProducto(models.Model):
    id_Producto = models.CharField(max_length=5,primary_key=True)
    nombre = models.CharField(max_length=15)
    precio = models.IntegerField()

    def __unicode__(self):
        return self.nombre

#productos vendidos
class ProductosVendidos(models.Model):
    nombre = models.CharField(max_length=25)
    precio = models.IntegerField()

    def __unicode__(self):
        return self.nombre
