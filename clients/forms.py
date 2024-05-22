# clients/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Cliente


class ClienteForm(UserCreationForm):
    email = forms.EmailField(required=True)
    telefone = forms.CharField(max_length=15)
    endereco = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'telefone', 'endereco']
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# class ClienteLoginForm(AuthenticationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'})
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={'class': 'form-control', 'placeholder': 'Senha'})
#     )


# class ProfissionalLoginForm(AuthenticationForm):
#     username = forms.CharField(
#         widget=forms.TextInput(
#             attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'})
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={'class': 'form-control', 'placeholder': 'Senha'})
#     )
