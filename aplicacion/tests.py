# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from aplicacion.models import receta, paciente, medico
from django.urls import reverse
from django.test import Client

APLICACION_RECETAS = 'receta_list'

class recetaTest(TestCase):

    def setUp(self):
    
        self._client = Client()
    
        medico.objects.all().delete()
        paciente.objects.all().delete()
        receta.objects.all().delete()
    
        med = medico.objects.create(nombreM="medico1")
        pac = paciente.objects.create(nombreP="paciente1")
        
        receta.objects.create(medico=med, paciente=pac)
        receta.objects.create(medico=med, paciente=pac)
        receta.objects.create(medico=med, paciente=pac)
        receta.objects.create(medico=med, paciente=pac)

    def test_aplicacion_recetas(self):
        
        lista_recetas = list(receta.objects.all())[-3:]
        
        response = self._client.get(reverse(APLICACION_RECETAS))

        for rec in lista_recetas:
            self.assertIn('<tr>\n<th>'+str(rec.id)+'</th>\n<td>'+rec.paciente.nombreP+'</td>\n<td>'+rec.medico.nombreM+'</td>\n</tr>', str(response.content))
            print ("    assert: %s"%str(rec.id))
