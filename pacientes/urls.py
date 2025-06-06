from django.urls import path
from . import views

urlpatterns = [
    path('pacientes/', views.paciente_list, name='paciente_list'),
    path('pacientes/novo/', views.paciente_create, name='paciente_create'),
    path('consultas/novo/', views.consulta_create, name='consulta_create'),
    path('consultas/relatorio/', views.relatorio_consultas_mes, name='relatorio_consultas_mes'),
    path('consultas/', views.consulta_list, name='consulta_list'),
]
