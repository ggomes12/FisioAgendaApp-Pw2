# clients/models.py
from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    # Armazena o arquivo no diretório 'uploads/usuario_<id>/perfil/<filename>'
    return f'uploads/usuario_{instance.user.id}/perfil/{filename}'


def prof_directory_path(instance, filename):
    # Armazena o arquivo no diretório 'uploads/usuario_<id>/perfil/<filename>'
    return f'uploads/usuario_{instance.user.id}/perfil/{filename}'


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, null=True, default=None)
    image = models.ImageField(
        upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Profissional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    # cpf = models.CharField(max_length=14, null=True, default=None)
    crefito = models.CharField(max_length=20, blank=True, null=True)
    especialidade = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(
        upload_to=prof_directory_path, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Consulta(models.Model):
    profissional = models.ForeignKey(
        Profissional, null=True, on_delete=models.SET_NULL)
    data = models.DateField()
    horario_inicial = models.TimeField(default='08:00:00')
    horario_final = models.TimeField(default='17:00:00')
    status = models.CharField(max_length=20, choices=[(
        'em aberto', 'Em Aberto'), ('concluido', 'Concluído')], default='em aberto')

    def __str__(self):
        return f"Consulta com {self.profissional.user.username} ({self.profissional.especialidade}) em {self.data} das {self.horario_inicial} às {self.horario_final}"

