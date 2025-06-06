from django.shortcuts import render, redirect
from .models import Paciente, Consulta
from .forms import PacienteForm, ConsultaForm
from django.utils import timezone
from datetime import datetime

# Listagem de pacientes

def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/paciente_list.html', {'pacientes': pacientes})

# Cadastro de paciente

def paciente_create(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = PacienteForm()
    return render(request, 'pacientes/paciente_form.html', {'form': form})

# Relatório de consultas do mês atual

def relatorio_consultas_mes(request):
    hoje = timezone.now()
    consultas = Consulta.objects.filter(
        data__year=hoje.year,
        data__month=hoje.month
    ).select_related('paciente')
    return render(request, 'pacientes/relatorio_consultas_mes.html', {'consultas': consultas, 'mes': hoje.strftime('%m/%Y')})

# Agendamento de consulta

def consulta_create(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_list')
    else:
        form = ConsultaForm()
    return render(request, 'pacientes/consulta_form.html', {'form': form})

# Listagem de consultas agendadas

def consulta_list(request):
    consultas = Consulta.objects.select_related('paciente').order_by('data')
    return render(request, 'pacientes/consulta_list.html', {'consultas': consultas})
