
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

import django
django.setup()

from aplicacion.models import medico, paciente, receta



def populate():

    cleanDatabase()
    
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
    c = receta.objects.get_or_create(medId=med, pacId=pac)[0]
    c.save()
        
    med = medico.objects.get_or_create(id=2)[0]
    pac = paciente.objects.get_or_create(id=1)[0]
    c = receta.objects.get_or_create(medId=med, pacId=pac)[0]
    c.save()
        
    med = medico.objects.get_or_create(id=1)[0]
    pac = paciente.objects.get_or_create(id=2)[0]
    c = receta.objects.get_or_create(medId=med, pacId=pac)[0]
    c.save()
        
    med = medico.objects.get_or_create(id=2)[0]
    pac = paciente.objects.get_or_create(id=2)[0]
    c = receta.objects.get_or_create(medId=med, pacId=pac)[0]
    c.save()
        
    med = medico.objects.get_or_create(id=3)[0]
    pac = paciente.objects.get_or_create(id=1)[0]
    c = receta.objects.get_or_create(medId=med, pacId=pac)[0]
    c.save()



def cleanDatabase():
    medico.objects.all().delete()
    paciente.objects.all().delete()
    receta.objects.all().delete()
        
# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()


