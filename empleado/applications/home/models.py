from django.db import models
# Create your models here.
class Prueba(models.Model):                         # herencia de models del modelo, especificamos crear una tabla
    titulo = models.CharField(max_length=30)        # atributo de mi tabla, tipo de dato y largo
    subtitulo = models.CharField(max_length=50)     # atributo de mi tabla
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo
