#populate database
# This code has to be placed in a file within the
# data/management/commands directory in your project.
# If that directory doesn't exist, create it.
# The name of the script is the name of the custom command,
# so let's call it populate.py. Another thing that has to be done
# is creating __init__.py files in both the management and commands
# directories, because these have to be Python packages.
#
# execute python manage.py  populate


from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from data.models import medico, paciente, receta

import commands
import dj_database_url
import psycopg2
import sys
import django
import random

django.setup()


# The name of this class is not optional must  be Command
# otherwise manage.py will not process it properly
class Command(BaseCommand):
    #  args = '<-no arguments>'
    # helps and arguments shown when command python manage.py help populate
    # is executed.
    help = 'This scripts populates de workflow database, no arguments needed.' \
           'Execute it with the command line python manage.py populate'

    def getParragraph(self, init, end):
        # getParragraph returns a parragraph, useful for testing
        if end > 445:
            end = 445
        if init < 0:
            init = 0
        return """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum."""[init:end]

    # handle is another compulsory name, This function will be
    # executed by default
    def handle(self, *args, **options):

        self.cleanDatabase()
        
        # Add medicos
        
        c = medico.objects.get_or_create(nombreM="medico1")[0]
    		c.save()
            
        c = medico.objects.get_or_create(nombreM="medico2")[0]
    		c.save()
            
        c = medico.objects.get_or_create(nombreM="medico3")[0]
    		c.save()
            
        c = medico.objects.get_or_create(nombreM="medico4")[0]
    		c.save()


        # Add pacientes
        
        c = paciente.objects.get_or_create(nombreP="paciente1")[0]
    		c.save()
            
        c = paciente.objects.get_or_create(nombreP="paciente2")[0]
    		c.save()


        # Add receta
        
        med = medico.objects.get_or_create(id=1)[0]
        pac = paciente.objects.get_or_create(id=1)[0]
        c = paciente.objects.get_or_create(medId=med, pacId=pac)[0]
    		c.save()
            
        med = medico.objects.get_or_create(id=2)[0]
        pac = paciente.objects.get_or_create(id=1)[0]
        c = paciente.objects.get_or_create(medId=med, pacId=pac)[0]
    		c.save()
            
        med = medico.objects.get_or_create(id=1)[0]
        pac = paciente.objects.get_or_create(id=2)[0]
        c = paciente.objects.get_or_create(medId=med, pacId=pac)[0]
    		c.save()
            
        med = medico.objects.get_or_create(id=2)[0]
        pac = paciente.objects.get_or_create(id=2)[0]
        c = paciente.objects.get_or_create(medId=med, pacId=pac)[0]
    		c.save()
            
        med = medico.objects.get_or_create(id=3)[0]
        pac = paciente.objects.get_or_create(id=1)[0]
        c = receta.objects.get_or_create(medId=med, pacId=pac)[0]
    		c.save()



    def cleanDatabase(self):
        medico.objects.all().delete()
        paciente.objects.all().delete()
        receta.objects.all().delete()


