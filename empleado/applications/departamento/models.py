from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)                            #Nombre sera como aparezca en el admin de django
    short_name = models.CharField('Nombre Corto',max_length=20, unique=True)    #Nombre corto, aparecera asi en el admin
    anulate = models.BooleanField('Anulado',default=False)                      #Se define por defecto en falso

    class Meta:
        verbose_name =  'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        unique_together = ('name','short_name')
        

    def __str__(self):
        return str(self.id) + '-' + self.name + '-' + self.short_name                    #Es una buena practica retornas los datos el id viene internamente en django
    
