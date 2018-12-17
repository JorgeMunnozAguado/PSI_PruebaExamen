# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from data.models import receta
from data.models import medico
from data.models import paciente

def receta():
    
    return render(request, 'receta.html', error="PRUEBA")
