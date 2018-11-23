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

from App.views import inicial,evento,atividade,visuevento,visuatividade,login,submissao,submeter,avaliacao,avaliar,gerencia,cadastro,certificado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', evento, name='url_evento'),
    path('atividade', atividade, name='url_atividade'),
    path('certificado', certificado, name='url_certificado'),
    path('visue', visuevento, name='url_visuevento'),
    path('visua', visuatividade, name='url_visuatividade'),
    path('login/', login, name='url_login'),
    path('cadastro/', cadastro, name='url_cadastro'),
    path('trabalhos/', submissao, name='url_submissao'),
    path('envio_trabalho/', submeter, name='url_submeter'),
    path('avaliar/', avaliar, name='url_avaliar'),
    path('avaliacao/', avaliacao, name='url_avaliacao'),
    path('gerencia/', gerencia, name='url_gerencia')
]
