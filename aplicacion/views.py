# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from aplicacion.models import receta
from aplicacion.models import medico
from aplicacion.models import paciente

def receta_list(request):
    
    _dict = {}
    
    try:
        lista_recetas =list(receta.objects.all())[-3:]

        _dict['recetas'] = lista_recetas
        _dict['error'] = None

    except:
        _dict['recetas'] = None
        _dict['error'] = "Error al acceder a la base de datos"
    
    return render(request, 'receta.html', _dict)
