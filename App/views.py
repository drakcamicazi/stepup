from django.shortcuts import render, redirect

# Create your views here.
from App.models import Participante,Usuario


def inicial(request):
    return render(request, 'index.html')

def login(request):
    data={}
    if request.method == 'POST':
        data["response"]={}
        data["response"]["id_mensagem"]=""
        data["response"]["id_validade"]=""
        data["response"]["senha_mensagem"]=""
        data["response"]["senha_validade"]=""
        p_cpf=request.POST.get("cpf","")
        u=Usuario.objects.get(cpf=p_cpf)
        if u.cpf == p_cpf:
            p_senha=request.POST.get("senha","")
            if u.senha == p_senha:
                data["response"]["id_mensagem"]="Logado como " + u.nome
                data["response"]["id_validade"]="valid"
                return render(request, 'login.html',data)
            else:
                data["response"]["senha_mensagem"]="Senha não corresponde!"
                data["response"]["senha_validade"]="invalid"
                return render(request, 'login.html',data)
        else:
            data["response"]["id_mensagem"]="Usuario não encontrado!"
            data["response"]["id_validade"]="invalid"

    else:
        data["response"]=""
    return render(request, 'login.html',data)

def cadastro(request):
    data={}
    if request.method == 'POST':
        p_nome=request.POST.get("nome","")
        p_email=request.POST.get("email","")
        p_sexo=request.POST.get("sexo","")
        p_cpf=request.POST.get("cpf","")
        p_senha=request.POST.get("senha","")
        p_data=request.POST.get("data","")

        u= Usuario.objects.create(nome=p_nome,cpf=p_cpf,sexo=p_sexo,email=p_email,senha=p_senha,data=p_data)
        u.save()
        data["response"]="Cadastrado com sucesso"
        return render(request, 'cadastro.html',data)
    else:
        data["response"]=""
        return render(request, 'cadastro.html',data)

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
