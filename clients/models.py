# clients/models.py
from django.contrib.auth.models import User
from django.db import models


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, null=True, default=None)

    def __str__(self):
        return self.user.username


class Profissional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    # cpf = models.CharField(max_length=14, null=True, default=None)
    crefito = models.CharField(max_length=20, blank=True, null=True)
    especialidade = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Consulta(models.Model):
    profissional = models.ForeignKey(
        Profissional, null=True, on_delete=models.SET_NULL)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"Consulta com {self.profissional.user.username} ({self.profissional.especialidade}) em {self.data} às {self.horario}"
