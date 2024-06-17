# clients/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from clients.models import Cliente, Consulta, Profissional


class ClienteForm(UserCreationForm):
    cpf = forms.CharField(max_length=14)
    email = forms.EmailField(required=True)
    telefone = forms.CharField(max_length=15)
    endereco = forms.CharField(max_length=255)
    

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'telefone', 'endereco',  'cpf']


class ProfissionalForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefone = forms.CharField(max_length=15)
    endereco = forms.CharField(max_length=255)
    especialidade = forms.CharField(max_length=100)
    crefito = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',
                  'telefone', 'endereco', 'especialidade', 'crefito']


class ConsultaForm(forms.ModelForm):
    profissional = forms.ModelChoiceField(
        queryset=Profissional.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Consulta
        fields = ['profissional', 'data', 'horario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }
