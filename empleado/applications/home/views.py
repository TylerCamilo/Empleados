from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba


#vistas es igual a logica del negocio

class IndexView(TemplateView):
    template_name='home/home.html'

class PruebaListView(ListView):             #SE HEREDA DE LA ListView
    template_name = 'home/lista.html'       #LO QUE VAMOS A LISTAR
    queryset=['a','camilo',1994]
    context_object_name='lista_prueba'      #ESTE ES EL QE LLAMO DESDE MI HTML

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name="test"

 