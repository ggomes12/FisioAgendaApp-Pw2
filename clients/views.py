from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from clients.forms import ClienteForm, ProfissionalForm
from clients.models import Cliente, Profissional
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def registration_client(request):
    if request.method == 'POST':
        formClient = ClienteForm(request.POST)
        if formClient.is_valid():
            user = formClient.save()
            Cliente.objects.create(
                user=user,
                telefone=formClient.cleaned_data['telefone'],
                endereco=formClient.cleaned_data['endereco'],
                cpf=formClient.cleaned_data['cpf']
            )
            login(request, user)
            return redirect('profile_clients')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        formClient = ClienteForm()
    return render(request, 'registration_client.html', {'form': formClient})


def registration_profissional(request):
    if request.method == 'POST':
        formProf = ProfissionalForm(request.POST)
        if formProf.is_valid():
            user= formProf.save()
            Profissional.objects.create(
                user=user,
                telefone=formProf.cleaned_data['telefone'],
                endereco=formProf.cleaned_data['endereco'],
                especialidade=formProf.cleaned_data['especialidade'],
                crefito=formProf.cleaned_data['crefito']
            )
            login(request, user)
            return redirect('profile_prof')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        formProf = ProfissionalForm()
    return render(request, 'registration_profissional.html', {'form': formProf})
   

def login_clients(request):
    if request.method == 'POST':
        formClient = AuthenticationForm(request, data=request.POST)
        if formClient.is_valid():
            user = formClient.get_user()
            if Cliente.objects.filter(user=user).exists():
                login(request, user)
                return redirect('profile_clients')
            else:
                messages.error(
                    request, 'Apenas clientes podem acessar esta página.')
        else:
            messages.error(
                request, 'Credenciais inválidas. Por favor, verifique suas informações.')
    else:
        formClient = AuthenticationForm()
    return render(request, 'login_clients.html', {'form': formClient})


def login_profissional(request):
    if request.method == 'POST':
        formProf = AuthenticationForm(request, data=request.POST)
        if formProf.is_valid():
            user = formProf.get_user()
            if Profissional.objects.filter(user=user).exists():
                login(request, user)
                return redirect('profile_prof')
            else:
                messages.error(
                    request, 'Apenas profissionais podem acessar esta página.')
        else:
            messages.error(
                request, 'Credenciais inválidas. Por favor, verifique suas informações.')
    else:
        formProf = AuthenticationForm()
    return render(request, 'login_profissional.html', {'form': formProf})



def logout_clients(request):
    logout(request)
    return redirect('login_clients')


def logout_prof(request):
    logout(request)
    return redirect('login_prof')


def pagina_nao_encontrada(request):
    return render(request, '404/404.html')


def profissionais_lista(request):
    # lógica para obter a lista de profissionais
    profissionais = []
    
    return render(request, 'profissionais_lista.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def news_blog(request):
    return render(request, 'blog-single.html')


@login_required
def profile_prof(request):
    return render(request, 'profile_profissional.html')


@login_required
def profile_client(request):
    return render(request, 'profile_clients.html')

# def esqueceu_senha(request):
#     return render(request, 'esqueceu_senha.html')
