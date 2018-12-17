# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from aplicacion.models import receta
from aplicacion.models import medico
from aplicacion.models import paciente

def receta():
    
    return render(request, 'receta.html', error="PRUEBA")
