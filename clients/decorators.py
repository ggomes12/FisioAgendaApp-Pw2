
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse

def client_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'cliente'):
            return view_func(request, *args, **kwargs)
        else:
            if not request.user.is_authenticated:
                # Redireciona para a página de login
                return redirect(reverse('login_clients'))
            # messages.error(
            #     request, 'Você não tem permissão para acessar esta página.')
            return redirect(reverse('login_clients'))
    return wrapper_func


def profissional_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'profissional'):
            return view_func(request, *args, **kwargs)
        else:
            if not request.user.is_authenticated:
                # Redireciona para a página de login
                return redirect(reverse('login_prof'))
            # messages.error(
            #     request, 'Você não tem permissão para acessar esta página.')
            return redirect(reverse('login_prof'))
    return wrapper_func
