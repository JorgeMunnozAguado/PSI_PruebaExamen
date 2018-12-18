# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Modelo del paciente
class paciente(models.Model):

    nombreP = models.CharField( max_length=500, blank=False )

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(paciente, self).save(*args, **kwargs)
        
    # class Meta:
    #     verbose_name_plural = 'Paciente'
    
    def __str__(self):
        return self.nombreP


# Modelo del medico
class medico(models.Model):

    nombreM = models.CharField( max_length=500, blank=False )

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(medico, self).save(*args, **kwargs)
        
    # class Meta:
    #     verbose_name_plural = 'Medico'
    
    def __str__(self):
        return self.nombreM


# Modelo del la receta
class receta(models.Model):

    medId = models.ForeignKey(medico, null=True )
    pacId = models.ForeignKey(paciente, null=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     super(medico, self).save(*args, **kwargs)
        
    # class Meta:
    #     verbose_name_plural = 'Receta'
    
    def __str__(self):
        return self.medId
        
        
        
        
