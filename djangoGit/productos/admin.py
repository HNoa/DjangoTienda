# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import DatosProducto, ProductosVendidos

# Register your models here.
admin.site.register(DatosProducto)

admin.site.register(ProductosVendidos)
