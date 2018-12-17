# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from aplicacion.models import receta
from aplicacion.models import medico
from aplicacion.models import paciente

def receta(request):
    
    _dict = {}
    
    try:
        lista_recetas = receta.objects.all()

        _dict['receta'] = lista_recetas
        _dict['error'] = None

    except:
        _dict['receta'] = None
        _dict['error'] = "Error al acceder a la base de datos"
    
    return render(request, 'receta.html', _dict)
