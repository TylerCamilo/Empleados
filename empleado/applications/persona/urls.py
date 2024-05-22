from django.urls import path
from .import views

app_name = "persona_app"

urlpatterns = [
    path('',
         views.InicioView.as_view(),
         name ='inicio'),

    path('listar-todo-empleados/',
         views.listAllEmpleados.as_view(),
         name='empleados_all'
         ),

    path('buscar-empleado/',
         views.listEmpleadosByKword.as_view(),
         name = 'busqueda'
         ),

    path('listar-habilidades-empleado/',
         views.ListHabilidadesdesEmpleado.as_view(),
         name = 'lista-habilidades'
         ),

    path('ver-empleado/<pk>',
         views.EmpleadoDetailView.as_view(),
         name = 'empleado_detail'
         ),

    path('add-empleado',
         views.EmpleadoCreateView.as_view(),
         name = 'agregar'),

    path('success',
         views.SuccessView.as_view(),
         name ='correcto'),

    path('update-empleado/<pk>',
         views.EmpleadoUpdateView.as_view(),
         name ='modificar_empleado'),

    path('delete-empleado/<pk>',
         views.EmpleadoDeleteView.as_view(),
         name ='eliminar_empleado'),

     path('list-by-area/<str:shortname>',
         views.ListByAreaEmpleado.as_view(),
         name ='empleados_area')
         
]