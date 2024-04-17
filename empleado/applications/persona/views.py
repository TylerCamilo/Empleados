from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import (ListView, DetailView,CreateView,TemplateView, UpdateView, DeleteView )
from .models import Empleado
from django.urls import reverse_lazy


#vista que carga la vista de inicio de mi app
class InicioView(TemplateView):
    template_name = "inicio.html"
    

class listAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 6
    ordering = 'first_name'

    def get_queryset(self):
        palabra_clave  = self.request.GET.get("kword", '')  #nos recupera lo que ingresemos en la caja.
        lista = Empleado.objects.filter(
            full_name__icontains=palabra_clave
        )
        print(lista)
        return lista

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

class SuccessView(TemplateView):
    template_name = "persona/success.html"

    

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    fields = ['first_name','last_name','job', 'Departamento','habilidades']
    success_url = reverse_lazy ('persona_app:correcto')

    def form_valid(self, form):
        #logica del proceos
        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)
    


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name','last_name','job', 'Departamento','habilidades']
    success_url = reverse_lazy ('persona_app:correcto')
   
    def post(self, request, *args, **kwargs):
            self.object = self.get_object()
            print('*******************METODO POST********************')
            print(request.POST)
            print(request.POST['last_name'])
            return super().post(request, *args, **kwargs)
        
    def form_valid(self, form):
        #logica del proceos
        print('*******************FORM_VALID********************')
        return super(EmpleadoUpdateView,self).form_valid(form)
    

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy ('persona_app:correcto')



