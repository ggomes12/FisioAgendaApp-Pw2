from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import ClienteForm
from .models import Cliente


def index(request):
    return render(request, 'index.html')

def registration_client(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            # Salva o cabloco
            user = form.save()
            # Cria um cliente associado ao cabloco
            cliente = Cliente.objects.create(
                user=user,
                telefone=form.cleaned_data['telefone'],
                endereco=form.cleaned_data['endereco']
            )
            # Realiza o login
            login(request, user)
            return redirect('profile_client')
    else:
        form = ClienteForm()
    return render(request, 'registration_client.html', {'form': form})


def registration_profissional(request):
    return render(request, 'registration_profissional.html')

def login_clients(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Autenticar o usuário
            user = form.get_user()
            login(request, user)
            return redirect('profile_client')
    else:
        form = AuthenticationForm()
    return render(request, 'login_clients.html', {'form': form})


def login_profissional(request):
    if request.method == 'POST':
        return render(request, 'index.html')
    return render(request, 'login_profissional.html')


def logout_clients(request):
    logout(request)
    return redirect('login_clients')


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

def profile_prof(request):
    return render(request, 'profile_profissional.html')

def profile_client(request):
    return render(request, 'profile_clients.html')

def esqueceu_senha(request):
    return render(request, 'esqueceu_senha.html')
