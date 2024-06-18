from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from clients import views



urlpatterns = [
     path('login_clients/', views.login_clients, name='login_clients'),
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
     path('contact-nos', views.contact, name='contact-nos'),
     path('marcar_consulta/<str:nome_fisio>/<str:especialidade>/',
         views.marcar_consulta, name='marcar_consulta'),
    path('marcar_concluido/<int:consulta_id>/',
         views.marcar_concluido, name='marcar_concluido'),
     #path('esqueceu_senha/', views.esqueceu_senha, name='esqueceu_senha'),
     path('404/', views.pagina_nao_encontrada, name='pagina_nao_encontrada'),
     path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
     path('news_blog/', views.news_blog, name='news_blog'),
     path("password_change", auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), name="password_change"),
     path("password_change_done/", auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name="password_change_done"),
     path('esqueceu_senha/', auth_views.PasswordResetView.as_view(template_name='esqueceu_senha.html'), name='esqueceu_senha'),
     path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
     path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
     path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
