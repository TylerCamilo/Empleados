from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import (ListView, DetailView,CreateView )
from .models import Empleado

class listAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    model =  Empleado

#lista de empleados por area
class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'

    def get_queryset(self):
        #El codigo que deseamos
        area=self.kwargs['shorname']
        lista = Empleado.objects.filter(
        Departamento__name=area
        )
        return lista
    
class listEmpleadosByKword(ListView):
    """#lista de empleados por palabra clave"""
    template_name ='persona/by_kword.html'
    context_object_name = 'empleados'               #nombre con el que se accede a la lista resultado
    
    def get_queryset(self):
        print("===========")
        palabra_clave  = self.request.GET.get("kword", '')  #nos recupera lo que ingresemos en la caja.
        print("===========", palabra_clave)
        lista = Empleado.objects.filter(
        first_name = palabra_clave
        )
        print('lista_resultado: ', lista )
        return lista
    
class ListHabilidadesdesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=8)
        print(empleado.habilidades.all())
        
        return (empleado.habilidades.all())

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        
        return context
    

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields = ('__all__')


