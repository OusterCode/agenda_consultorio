from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    endereco = models.CharField(max_length=200, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    data = models.DateTimeField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.paciente.nome} - {self.data.strftime('%d/%m/%Y %H:%M')}"
