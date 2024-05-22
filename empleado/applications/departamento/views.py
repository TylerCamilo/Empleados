from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print('====================Estamos en el form valid')

        #instancia del modelo departamento
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            short_name = form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            Departamento = depa
        )
        return super(NewDepartamentoView, self).form_valid(form)
    
    
class DepartamentoListView(ListView):
        model = Departamento
        template_name = "departamento/lista.html"
        context_object_name = 'departamentos'
    