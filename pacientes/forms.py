from django import forms
from .models import Paciente, Consulta
import re
from django.core.exceptions import ValidationError
from django.utils import timezone

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'data_nascimento', 'telefone', 'email', 'endereco', 'observacoes']

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        # Formato: +Cód pais DD 9 XXXXXXXX (ex: +55 11 9 12345678)
        pattern = r'^\+\d{2} \d{2} 9 \d{8}$'
        if telefone and not re.match(pattern, telefone):
            raise ValidationError('O telefone deve estar no formato: +55 11 9 12345678')
        return telefone

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'data', 'observacoes']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def clean(self):
        cleaned_data = super().clean()
        paciente = cleaned_data.get('paciente')
        data = cleaned_data.get('data')
        if paciente and data:
            # Verifica se já existe consulta para o paciente no mesmo dia
            consultas_no_dia = Consulta.objects.filter(
                paciente=paciente,
                data__date=data.date()
            )
            if self.instance.pk:
                consultas_no_dia = consultas_no_dia.exclude(pk=self.instance.pk)
            if consultas_no_dia.exists():
                raise ValidationError('Já existe uma consulta agendada para este paciente neste dia.')
            # Verifica intervalo de 60 minutos entre consultas do mesmo paciente
            inicio = data - timezone.timedelta(minutes=59)
            fim = data + timezone.timedelta(minutes=59)
            conflito = Consulta.objects.filter(
                paciente=paciente,
                data__range=(inicio, fim)
            )
            if self.instance.pk:
                conflito = conflito.exclude(pk=self.instance.pk)
            if conflito.exists():
                raise ValidationError('O intervalo entre consultas deve ser de pelo menos 60 minutos para o mesmo paciente.')
        return cleaned_data
