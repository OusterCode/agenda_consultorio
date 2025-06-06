from django.contrib import admin
from .models import Paciente, Consulta

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'telefone', 'email')
    search_fields = ('nome', 'email')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data')
    list_filter = ('data',)
    search_fields = ('paciente__nome',)
