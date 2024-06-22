
# projeto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from clients import views as client_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', client_views.index, name='index'),  # Home
    # Inclui as URLs da aplicação clients
    path('clients/', include('clients.urls')),
    #path('clients/', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

pag_not_found = "clients.views.pagina_nao_encontrada"

handler500 = "clients.views.handler500"
