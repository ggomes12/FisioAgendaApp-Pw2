from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from clients.forms import ClienteForm, ProfissionalForm
from clients.models import Cliente
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def registration_client(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            try:
                # Valida a senha usando os validadores configurados
                form.clean_password2()
                # Salva o usuário
                user = form.save()
                # Cria um cliente associado ao usuário
                Cliente.objects.create(
                    user=user,
                    telefone=form.cleaned_data['telefone'],
                    endereco=form.cleaned_data['endereco'],
                    cpf=form.cleaned_data['cpf']
                )
                # Realiza o login
                login(request, user)
                messages.success(
                    request, 'Cadastro realizado com sucesso! Bem-vindo(a), {}!'.format(user.username))
                return redirect('profile_clients')
            except ValidationError as e:
                for error in e:
                    messages.error(request, error)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = ClienteForm()
    return render(request, 'registration_client.html', {'form': form})


def registration_profissional(request):
    if request.method == 'POST':
        form = ProfissionalForm(request.POST)
        if form.is_valid():
            try:
                # Valida a senha usando os validadores configurados
                form.clean_password2()
                # Salva o usuário
                user = form.save()
                # Cria um cliente associado ao usuário
                Cliente.objects.create(
                    user=user,
                    telefone=form.cleaned_data['telefone'],
                    endereco=form.cleaned_data['endereco'],
                    especialidade=form.cleaned_data['especialidade'],
                    crefito=form.cleaned_data['crefito'],
                )
                # Realiza o login
                login(request, user)
                messages.success(
                    request, 'Cadastro realizado com sucesso! Bem-vindo(a), {}!'.format(user.username))
                return redirect('profile_prof')
            except ValidationError as e:
                for error in e:
                    messages.error(request, error)
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = ProfissionalForm()
    return render(request, 'registration_profissional.html', {'form': form})
   
def login_clients(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar o usuário
            user = form.get_user()
            login(request, user)
            return redirect('profile_clients')
    else:
        form = AuthenticationForm()
    return render(request, 'login_clients.html', {'form': form})


def login_profissional(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar o usuário
            user = form.get_user()
            login(request, user)
            return redirect('profile_prof')
    else:
        form = AuthenticationForm()
    return render(request, 'login_profissional.html', {'form': form})


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
