# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from aplicacion.models import medico, paciente, receta

admin.site.register(medico)
admin.site.register(paciente)
admin.site.register(receta)
