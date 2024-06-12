# clients/urls.py
from django.urls import path
from clients import views

urlpatterns = [
    path('login/', views.login_clients, name='login_clients'),
    path('login_profissional/', views.login_profissional,
         name='login_prof'),
    path('logout_clients/', views.logout_clients, name='logout_clients'),
    path('logout_prof/', views.logout_prof, name='logout_prof'),
    path('profissionais_lista/', views.profissionais_lista,
         name='profissionais_lista'),
    path('profile_prof/', views.profile_prof, name='profile_prof'),
    path('profile_clients/', views.profile_client, name='profile_clients'),
    path('registration_profissional/', views.registration_profissional,
         name='registration_prof'),
    path('registration_client/', views.registration_client,
         name='registration_client'),
    path('esqueceu_senha/', views.esqueceu_senha, name='esqueceu_senha'),
    path('404/', views.pagina_nao_encontrada, name='pagina_nao_encontrada'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    path('news_blog/', views.news_blog, name='news_blog'),
]
