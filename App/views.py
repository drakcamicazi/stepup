from django.shortcuts import render, redirect

# Create your views here.
from App.models import Participante


def inicial(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def evento(request):
    return render(request, 'eventos.html')

def certificado(request):
    return render(request, 'certificados.html')

def visuevento(request):
    return render(request, 'visualizarEventos.html')

def atividade(request):
    return render(request, 'atividades.html')

def criarativi(request):
    return render(request, 'nova_atividade.html')

def visuatividade(request):
    return render(request, 'visualizarAtividade.html')

def submissao(request):
    return render(request, 'submissao.html')

def avaliar(request):
    return render(request, 'avaliar.html')

def avaliacao(request):
    return render(request, 'avaliador.html')

def gerencia(request):
    return render(request, 'gerencia_trabalho.html')

def submeter(request):
    return render(request, 'submeter.html')

def gerarCracha(request):
    data = {'participantes': Participante.objects.all()}
    return render(request, 'gerar_cracha.html', data)

def loginAdmin(request):
    return render(request, 'admin/loginadmin.html')

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def campus(request):
    return render(request, 'admin/campus.html')

def servidores(request):
    return render(request, 'admin/servidores.html')

def novoevento(request):
    return render(request, 'admin/novoevento.html')
