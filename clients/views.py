from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from clients.forms import ClienteForm, ProfissionalForm
from clients.models import Cliente, Profissional
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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

def pagina_nao_encontrada(request, exception):
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
    # Obtém os parâmetros de busca da URL
    txt_nome = request.GET.get('nome')
    txt_especialidade = request.GET.get('especialidade')

    # Filtra a lista de profissionais com base nos parâmetros fornecidos
    clients_profissional_list = Profissional.objects.all()
    if txt_nome:
        clients_profissional_list = clients_profissional_list.filter(user__username__icontains=txt_nome)
    if txt_especialidade:
        clients_profissional_list = clients_profissional_list.filter(especialidade__icontains=txt_especialidade)

    # Ordena a lista de profissionais
    clients_profissional_list = clients_profissional_list.order_by('user__username')

    # Configura a paginação
    paginator = Paginator(clients_profissional_list, 10)  # 1 profissional por página (ajuste conforme necessário)

    page = request.GET.get('page')
    try:
        clients_profissional = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, exibe a primeira página.
        clients_profissional = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo (por exemplo, 9999), exibe a última página de resultados.
        clients_profissional = paginator.page(paginator.num_pages)

    # Renderiza o template com os profissionais paginados e os parâmetros de busca
    return render(request, 'profile_clients.html', {
        'clients_profissional': clients_profissional,
        'txt_nome': txt_nome,
        'txt_especialidade': txt_especialidade,
    })


def contact(request):
    return render(request, 'contact.html')