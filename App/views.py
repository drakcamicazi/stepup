from django.shortcuts import render, redirect

# Create your views here.
from App.models import Participante,Usuario


def deslogar(request):
    request.session["logado"]=False
    request.session["logado_cpf"]=""
    return redirect(login)

def login(request):
    # Definindo coleção de dados para ser passar nos "render"!
    data={}
    # Verificando se a requisição e via post!
    if request.method == 'POST':
        # Criando coleção de valores para retorno ao usuario!
        data["response"]={}
        # Adquirindo o valor recebido pela request!
        p_cpf=request.POST.get("cpf","")
        # Verificando se o usuario existe no banco!
        existencia=Usuario.objects.filter(cpf=p_cpf).exists()
        if existencia == True:
            # Pegando as informações do usuario!
            u=Usuario.objects.get(cpf=p_cpf)
            # Adquirindo a senha recebida na request!
            p_senha=request.POST.get("senha","")
            # Comparando senha para ver se corresponde!
            if u.senha == p_senha:
                # Defini na session o cpf do usuario logado e autenticado!
                request.session["logado_cpf"]=u.cpf
                request.session["logado"]=True
                # Redireciona para pagina de eventos do site
                return redirect(evento)
            else:
                # Definindo retorno de senha não correspondida
                data["response"]["usuario"]=p_cpf
                data["response"]["senha_mensagem"]="Senha não corresponde!"
                data["response"]["senha_validade"]="invalid"
                # Retornando pagina
                return render(request, 'login.html',data)
        else:
            # Definindo retorno de usuario não existente no banco
            data["response"]["id_mensagem"]="Usuario não encontrado!"
            data["response"]["id_validade"]="invalid"
            # Retornando pagina
            return render(request, 'login.html',data)
    else:
        if "logado" in request.session:
            if request.session["logado"]==True:
                # Redireciona para pagina de eventos do site apos verificar 
                return redirect(evento)    
            else:
                # Retornando pagina padrão
                return render(request, 'login.html',data)
        else:
            # Retornando pagina padrão
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
        request.session["logado_cpf"]=u.cpf
        request.session["logado"]=True
        return redirect(login)
    else:
        if "logado" in request.session:
            if request.session["logado"]==True:
                # Redireciona para pagina de eventos do site apos verificar 
                return redirect(evento)    
            else:
                # Retornando pagina padrão
                return render(request, 'cadastro.html',data)
        else:
            # Retornando pagina padrão
            return render(request, 'cadastro.html',data)

def evento(request):
    data={}
    if "logado" in request.session:
        if request.session["logado"]==True:
            r_cpf=request.session["logado_cpf"]
            u=Usuario.objects.get(cpf=r_cpf)
            data["nome"]=u.nome
            return render(request, 'eventos.html',data)     
        else:
            # Retornando pagina padrão
            return redirect(login)
    else:
        # Retornando pagina de login
        return redirect(login)

def certificado(request):
    data={}
    if "logado" in request.session:
        if request.session["logado"]==True:
            r_cpf=request.session["logado_cpf"]
            u=Usuario.objects.get(cpf=r_cpf)
            data["nome"]=u.nome
            return render(request, 'certificados.html',data)   
        else:
            # Retornando pagina padrão
            return redirect(login)
    else:
        # Retornando pagina de login
        return redirect(login)
    
def atividade(request):
    data={}
    if "logado" in request.session:
        if request.session["logado"]==True:
            r_cpf=request.session["logado_cpf"]
            u=Usuario.objects.get(cpf=r_cpf)
            data["nome"]=u.nome
            return render(request, 'atividades.html',data)   
        else:
            # Retornando pagina padrão
            return redirect(login)
    else:
        # Retornando pagina de login
        return redirect(login)

def visuevento(request):
    data={}
    if "logado" in request.session:
        if request.session["logado"]==True:
            if request.method == "POST":
                r_cpf=request.session["logado_cpf"]
                u=Usuario.objects.get(cpf=r_cpf)
                data["nome"]=u.nome
                return render(request, 'visualizarEvento.html',data)   
            else:
                return redirect(evento)   
        else:
            # Retornando pagina padrão
            return redirect(login)
    else:
        # Retornando pagina de login
        return redirect(login)


def criarativi(request):
    r_cpf=request.session["logado_cpf"]
    u=Usuario.objects.get(cpf=r_cpf)
    data={}
    data["nome"]=u.nome
    return render(request, 'nova_atividade.html', data)

def visuatividade(request):
    data={}
    if "logado" in request.session:
        if request.session["logado"]==True:
            if request.method == "POST":
                r_cpf=request.session["logado_cpf"]
                u=Usuario.objects.get(cpf=r_cpf)
                data["nome"]=u.nome
                return render(request, 'visualizarAtividade.html',data)   
            else:
                return redirect(atividade)   
        else:
            # Retornando pagina padrão
            return redirect(login)
    else:
        # Retornando pagina de login
        return redirect(login)

def submissao(request):
    r_cpf=request.session["logado_cpf"]
    u=Usuario.objects.get(cpf=r_cpf)
    data={}
    data["nome"]=u.nome
    return render(request, 'submissao.html', data)

def avaliar(request):
    r_cpf=request.session["logado_cpf"]
    u=Usuario.objects.get(cpf=r_cpf)
    data={}
    data["nome"]=u.nome
    return render(request, 'avaliar.html', data)

def avaliacao(request):
    r_cpf=request.session["logado_cpf"]
    u=Usuario.objects.get(cpf=r_cpf)
    data={}
    data["nome"]=u.nome
    return render(request, 'avaliador.html', data)

def gerencia(request):
    r_cpf=request.session["logado_cpf"]
    u=Usuario.objects.get(cpf=r_cpf)
    data={}
    data["nome"]=u.nome
    return render(request, 'gerencia_trabalho.html', data)

def submeter(request):
    r_cpf=request.session["logado_cpf"]
    u=Usuario.objects.get(cpf=r_cpf)
    data={}
    data["nome"]=u.nome
    return render(request, 'submeter.html', data)

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
