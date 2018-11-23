from django.shortcuts import render, redirect
#from .form import PessoaForm

# Create your views here.
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
