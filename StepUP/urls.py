"""StepUP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import  include, url
from django.contrib import admin

from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.conf import settings

from App.views import evento, atividade, login, submissao, submeter, avaliacao, deslogarAdmin, \
    avaliar, gerencia, cadastro, certificado, gerarCracha, criarativi, loginAdmin, dashboard, campus, servidores, novoevento, \
    deslogar,departamento,novocampus,novodepartamento,novoservidor,perfil,procura

urlpatterns = [
    # Parte administrativa
        path('admin/',loginAdmin,name="url_loginadmin" ),
        path('admin/deslogar', deslogarAdmin, name='url_deslogaradmin'),
        path('admin/dashboard/',dashboard,name="url_dashboard" ),
        path('admin/novo_evento/',novoevento,name="url_novoevento" ),
        path('admin/novo_campus/',novocampus,name="url_novocampus" ),
        path('admin/novo_departamento/',novodepartamento,name="url_novodepartamento" ),
        path('admin/novo_servidor/',novoservidor,name="url_novoservidor" ),
        path('admin/campus/',campus,name="url_campus" ),
        path('admin/departamentos/',departamento,name="url_departamentos" ),
        path('admin/servidores/',servidores,name="url_servidores" ),
    # Parte de Login e autenticação
        path('', login, name='url_login'),
        path('deslogar/', deslogar, name='url_deslogar'),
        path('cadastro/', cadastro, name='url_cadastro'),
    # Paginas de Navegação
        # Perfil
            path('perfil/', perfil, name='url_perfil'),
        # Eventos
            path('eventos/', evento, name='url_evento'),
            # path('evento/', visuevento, name='url_visuevento'), Inutilizavel agora!
        # Atividades
            path('atividades/', atividade, name='url_atividade'),
            # path('atividade/', visuatividade, name='url_visuatividade'),Inutilizavel agora!
            path('criar_atividade/', criarativi, name='url_criarativi'),
        # Trabalhos
            path('trabalhos/', submissao, name='url_submissao'),
            path('envio_trabalho/', submeter, name='url_submeter'),
            path('avaliar/', avaliar, name='url_avaliar'),
            path('avaliacao/', avaliacao, name='url_avaliacao'),
            path('gerencia/', gerencia, name='url_gerencia'),
        # Certificados
            path('certificado/', certificado, name='url_certificado'),
        # Cracha e outros
            path('cracha/', gerarCracha, name='url_cracha'),
        
        path('procura', procura, name='url_procurar'),

]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)