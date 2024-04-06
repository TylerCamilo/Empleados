from django.db import models
from applications.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name =  'Habilidad'
        verbose_name_plural = 'Habilidades Empleadosss'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '. ' + self.habilidad 

# Create your models here.
class Empleado(models.Model):
    #""" Modelo para tabla empleado """
    first_name = models.CharField('Nombres',max_length=60)
    last_name = models.CharField('Apellidos',max_length=60)
    full_name = models.CharField('Nombre Completo',max_length=60, blank=True)
    JOB_CHOICES = [
        ('0', 'CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
        ('4', 'INGENIERO')
    ]
    job = models.CharField('Trabajo', max_length=50,choices= JOB_CHOICES)
    #LA RELACION FOERING KEY con djaneiro se digita fk para el formato
    #Esta relacion es de uno a muchos
    Departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    #sql3lite no soporta imagenes, entonces quedara para app en el futuro
    #avatar = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
    habilidades = models.ManyToManyField(Habilidades)


    class Meta:
        verbose_name =  'Empleado'
        verbose_name_plural = 'Empleadosss'
        ordering = ['last_name']
        unique_together = ('first_name','last_name')

    def __str__(self,):
        return str(self.id) + ' ' + self.first_name + ' ' + self.last_name 