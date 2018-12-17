# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from aplicacion.models import receta
from aplicacion.models import medico
from aplicacion.models import paciente

def receta(request):
    
    _dict = {'category': None,
             'error': "prueba"
	}
    
    return render(request, 'receta.html', _dict)
