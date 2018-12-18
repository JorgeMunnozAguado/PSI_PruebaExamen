# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Modelo del paciente
class paciente(models.Model):

    nombreP = models.CharField( max_length=500, blank=False )
    
    def __str__(self):
        return self.nombreP


# Modelo del medico
class medico(models.Model):

    nombreM = models.CharField( max_length=500, blank=False )
    
    def __str__(self):
        return self.nombreM


# Modelo del la receta
class receta(models.Model):

    medico = models.ForeignKey(medico, null=True )
    paciente = models.ForeignKey(paciente, null=True)
    
    def __str__(self):
        return str(self.id)
        
        
        
        
