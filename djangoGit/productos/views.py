# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.generic import CreateView

from django.shortcuts import render, get_object_or_404
from .models import DatosProducto, ProductosVendidos

# Create your views here.

def index(request):
    return render(request, "templates/djangoGit/index.html")

def resultado(request):
    datos = DatosProducto.objects.all()
    return render(request, "templates/djangoGit/resultado.html", {"productos":datos})

def principal(request):
    return render(request, "templates/djangoGit/principal.html")

#    model = ProductosVendidos

def sumar(request):
    
    return render(request, "templates/djangoGit/sumar.html")

def detalle(request):
    return render(request, "templates/djangoGit/detalle.html")
