# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from aplicacion.models import receta, paciente, medico
from django.urls import reverse


APLICACION_RECETAS = 'recetas'

class AnimalTestCase(TestCase):

borre todos los medicos, pacientes y recetas
cree el m´edico (1,’medico1’)
cree el paciente (1,’paciente1’)
cree la receta (1,1,1)
cree la receta (2,1,1)
cree la receta (3,1,1)
cree la receta (4,1,1)
acceda a la vista relacionada con el URL $PROJECT URL/aplicacion/receta/
compruebe que las recetas devueltas son las correctas.


    def setUp(self):
    
        medico.objects.all().delete()
        paciente.objects.all().delete()
        receta.objects.all().delete()
    
        medico.objects.create(nombreM="medico1")
        paciente.objects.create(nombreP="paciente1")
        
        receta.objects.create(medico=medico, paciente=paciente)
        receta.objects.create(medico=medico, paciente=paciente)
        receta.objects.create(medico=medico, paciente=paciente)
        receta.objects.create(medico=medico, paciente=paciente)

    def test_aplicacion_recetas(self):
        
        response = self._client.get(reverse(APLICACION_RECETAS), follow=True)
        print "Response: " + str(response.content)