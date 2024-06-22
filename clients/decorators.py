
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse
from functools import wraps

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


def update_profile_required(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'clients'):            
            return view_func(request, *args, **kwargs)
        else:
            messages.error(
                request, 'Você não tem permissão para acessar esta página.')
            if not request.user.is_authenticated:
                return redirect(reverse('login_clients'))
        return redirect(reverse('login_clients'))
    return wrapper_func


def update_professional_profile_required(view_func):
    @wraps(view_func)
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'professional'):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(
                request, 'Você não tem permissão para acessar esta página.')
            if not request.user.is_authenticated:
                return redirect(reverse('login_prof'))

        return redirect(reverse('login_prof'))
    return wrapper_func
