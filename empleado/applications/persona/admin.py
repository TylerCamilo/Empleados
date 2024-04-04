from django.contrib import admin
from .models import Empleado, Habilidades
		
# Register your models here.

class HabilidadesAdmin(admin.ModelAdmin):
    list_display = (
        'habilidad',
    )
    search_fields = ('habilidad',)

admin.site.register(Habilidades, HabilidadesAdmin)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'Departamento',
        'job',
        'full_name',
        'id'
    )

    def full_name(self,obj):
        #toda la operacion de la funcion
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name


    search_fields = ('last_name',)
    list_filter = ('job', 'habilidades','Departamento')               #dentro del parentesis va el registro donde quiero que haga busqueda
    filter_horizontal = ('habilidades',) #Solo funciona de muchis a muchos

admin.site.register(Empleado, EmpleadoAdmin)

