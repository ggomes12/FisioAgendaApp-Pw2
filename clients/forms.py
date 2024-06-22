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


class UserProfileForm(forms.ModelForm):
    telefone = forms.CharField(max_length=15, required=False)
    endereco = forms.CharField(max_length=255, required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            try:
                cliente = self.instance.cliente
                self.fields['telefone'].initial = cliente.telefone
                self.fields['endereco'].initial = cliente.endereco
            except Cliente.DoesNotExist:
                pass

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        
        if self.cleaned_data['telefone'] and self.cleaned_data['endereco']:
            try:
                cliente = user.cliente if hasattr(user, 'cliente') else Cliente(user=user)
                cliente.telefone = self.cleaned_data['telefone']
                cliente.endereco = self.cleaned_data['endereco']
                cliente.save()
            except Cliente.DoesNotExist:
                pass

        if self.cleaned_data['image']:
            try:
                cliente = user.cliente if hasattr(user, 'cliente') else Cliente(user=user)
                cliente.image = self.cleaned_data['image']
                cliente.save()
            except Cliente.DoesNotExist:
                pass

        if commit:
            user.save()
        return user
    

class ProfessionalProfileForm(forms.ModelForm):
    telefone = forms.CharField(max_length=15, required=False)
    endereco = forms.CharField(max_length=255, required=False)
    especialidade = forms.CharField(max_length=100, required=False)
    crefito = forms.CharField(max_length=20, required=False)
    image = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email']
        
    def __init__(self, *args, **kwargs):
        super(ProfessionalProfileForm, self).__init__(*args, **kwargs)
        
        if self.instance.pk:
            try:
                profissional = self.instance.profissional
                self.fields['telefone'].initial = profissional.telefone
                self.fields['endereco'].initial = profissional.endereco
                self.fields['especialidade'].initial = profissional.especialidade
                self.fields['crefito'].initial = profissional.crefito
            except Profissional.DoesNotExist:
                pass

    def save(self, commit=True):
        user = super(ProfessionalProfileForm, self).save(commit=False)

        if self.cleaned_data['telefone'] and self.cleaned_data['endereco']:
            try:
                profissional = user.profissional if hasattr(user, 'profissional') else Profissional(user=user)
                profissional.telefone = self.cleaned_data['telefone']
                profissional.endereco = self.cleaned_data['endereco']
                profissional.especialidade = self.cleaned_data['especialidade']
                profissional.crefito = self.cleaned_data['crefito']
                profissional.save()
            except Profissional.DoesNotExist:
                pass

        if self.cleaned_data['image']:
            try:
                profissional = user.profissional if hasattr(user, 'profissional') else Profissional(user=user)
                profissional.image = self.cleaned_data['image']
                profissional.save()
            except Profissional.DoesNotExist:
                pass

        if commit:
            user.save()
        return user
    