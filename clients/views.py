from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from clients.forms import ClienteForm, ProfissionalForm, ConsultaForm, UserProfileForm, ProfessionalProfileForm, CustomizadoPasswordChangeForm
from clients.models import Cliente, Profissional, Consulta
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .decorators import client_required, profissional_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    return render(request, 'index.html')


def voltar(request):
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return HttpResponseRedirect(referer)
    else:
        return HttpResponseRedirect(reverse('index'))

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
            user = formProf.save()
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

def handler500(request):
    return render(request, '500.html')

def profissionais_lista(request):
    # lógica para obter a lista de profissionais
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
    paginator = Paginator(clients_profissional_list, 10)  # 10 profissional por página

    page = request.GET.get('page')
    try:
        clients_profissional = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, exibe a primeira página.
        clients_profissional = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo (por exemplo, 9999), exibe a última página de resultados.
        clients_profissional = paginator.page(paginator.num_pages)
    
    return render(request, 'profissionais_lista.html', {
        'clients_profissional': clients_profissional})

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def news_blog(request):
    return render(request, 'blog-single.html')


@login_required
@profissional_required
@never_cache
def profile_prof(request):
    profissional = request.user.profissional
    consultas_list = Consulta.objects.filter(profissional=profissional).order_by('data')

    # Configura a paginação
    paginator = Paginator(consultas_list, 10)  # 10 profissional por página

    page = request.GET.get('page')
    try:
        consultas = paginator.page(page)
    except PageNotAnInteger:
        # Se a página não for um inteiro, exibe a primeira página.
        consultas = paginator.page(1)
    except EmptyPage:
        # Se a página estiver fora do intervalo (por exemplo, 9999), exibe a última página de resultados.
        consultas = paginator.page(paginator.num_pages)

    return render(request, 'profile_profissional.html', {
        'profissional': profissional,
        'consultas': consultas,
    })


@login_required
def marcar_concluido(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if consulta.profissional.user == request.user:
        consulta.status = 'concluido'
        consulta.save()
        messages.success(request, 'Consulta marcada como concluída.')
    else:
        messages.error(
            request, 'Você não tem permissão para concluir esta consulta.')

    return redirect('profile_prof')


@login_required
@client_required
@never_cache
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
    paginator = Paginator(clients_profissional_list, 10)  # 10 profissional por página

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


def marcar_consulta(request, nome_fisio, especialidade):
    try:
        profissional = Profissional.objects.get(
            user__username=nome_fisio, especialidade=especialidade)
    except Profissional.DoesNotExist:
        messages.error(request, 'Profissional não encontrado.')
        return redirect('marcar_consulta')

    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            nova_consulta = form.save(commit=False)
            nova_consulta.profissional = profissional  

            data = form.cleaned_data['data']
            horario_inicial = form.cleaned_data['horario_inicial']
            horario_final = form.cleaned_data['horario_final']

            # Verifica se ja tem prof com agendamento para data e hora
            if Consulta.objects.filter(data=data, horario_inicial=horario_inicial, horario_final=horario_final, profissional=profissional).exists():
                messages.error(
                    request, 'Já existe uma consulta agendada para este médico, dia e horário.')
            else:
                nova_consulta.save()
                messages.success(request, 'Consulta marcada com sucesso!')
                return redirect('marcar_consulta', nome_fisio=nome_fisio, especialidade=especialidade)
        else:
            messages.error(
                request, 'Erro no formulário. Verifique os dados e tente novamente.')
    else:
        form = ConsultaForm(initial={'profissional': profissional})

    return render(request, 'agendamento_consult.html', {'form': form, 'profissional': profissional})


@login_required
@client_required
def update_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
            return redirect('profile_clients')
        else:
            messages.error(
                request, 'Erro ao atualizar perfil. Verifique os campos informados.')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'update_profile.html', {'form': form})


@login_required
@profissional_required
def update_professional_profile(request):
    if request.method == 'POST':
        form = ProfessionalProfileForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Perfil atualizado com sucesso.')
            return redirect('profile_prof')
        else:
            messages.error(
                request, 'Erro ao atualizar perfil. Verifique os campos informados.')
    else:
        form = ProfessionalProfileForm(instance=request.user)
    
    return render(request, 'update_professional_profile.html', {'form': form})

def services(request):
    return render(request, 'services.html')


def casos_emergencia(request):
    return render(request, 'casos_emergencia.html')


def horario_atendimentos(request):
    return render(request, 'horario_atendimentos.html')


def descricao(request):
    return render(request, 'descricao.html')


@login_required
def password_change(request):
    if request.method == 'POST':
        form = CustomizadoPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # mantem o usuário logado após a troca de senha
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi atualizada com sucesso!')
            return redirect('password_change')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = CustomizadoPasswordChangeForm(request.user)
    return render(request, 'password_change_form.html', {'form': form})

