from django.shortcuts import render, redirect
from django.http import JsonResponse
from .form import EventoModelForm,UsuarioModelForm,AtividadeModelForm

# Create your views here.
from App.models import Usuario,Evento,Participante,Administrador,Campus,Departamento,Servidor


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
        form=UsuarioModelForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            request.session["logado_cpf"]=request.POST.get('cpf')
            request.session["logado"]=True
            return redirect(login)
        else:
            data['form']=UsuarioModelForm()
            data['erro']="erro"
            return render(request, 'cadastro.html',data)
    else:
        if "logado" in request.session:
            if request.session["logado"]==True:
                # Redireciona para pagina de eventos do site apos verificar 
                return redirect(login)    
            else:
                data['form']=UsuarioModelForm()
                # Retornando pagina padrão
                return render(request, 'cadastro.html',data)
        else:
            data['form']=UsuarioModelForm()
            # Retornando pagina padrão
            return render(request, 'cadastro.html',data)



def evento(request):
    if "logado" in request.session:
        data={}
        if request.session["logado"]==True:
            data["eventoslista"]=Evento.objects.all()
            data["logadoUsuario"]=Usuario.objects.get(cpf=request.session["logado_cpf"])
            if "evento" in request.GET:
                data["evento"]=Evento.objects.get(nome=request.GET.get("evento"))
                return render(request, 'visualizarEvento.html',data)   
            else:
                return render(request, 'eventos.html',data)     
        else:
            # Retornando pagina padrão
            return redirect(login)
    else:
        # Retornando pagina de login
        return redirect(login)



def perfil(request):
    if "logado" in request.session:
        data={}
        if request.session["logado"]==True:
            data["logadoUsuario"]=Usuario.objects.get(cpf=request.session["logado_cpf"])
            return render(request, 'perfil.html',data) 
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
            data["logadoUsuario"]=u
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
            data["logadoUsuario"]=u
            if "atividade" in request.GET:
                data['atividade']=request.GET.get("atividade","")
                return render(request, 'visualizarAtividade.html',data)   
            else:
                return render(request, 'atividades.html',data)   
        else:
            # Retornando pagina padrão
            return redirect(login)
    else:
        # Retornando pagina de login
        return redirect(login)

def procura(request):
    j={"evento":Evento.objects.all()}
    return JsonResponse(j)

def criarativi(request):
    data={}
    if "logado" in request.session:
        if request.session["logado"]==True:
            if request.method=="POST":
                form=AtividadeModelForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect(atividade)
                else:
                    data['erro']='Alguma informação esta invalida!'
                    return render(request, 'nova_atividade.html', data)
            else:
                u=Usuario.objects.get(cpf=request.session["logado_cpf"])
                data["logadoUsuario"]=u
                data['form']=AtividadeModelForm()
                return render(request, 'nova_atividade.html', data)
        else:
            # Retornando pagina padrão
            return redirect(login)
    else:
        # Retornando pagina de login
        return redirect(login)



def submissao(request):
    r_cpf=request.session["logado_cpf"]
    data={}
    u=Usuario.objects.get(cpf=r_cpf)
    data["logadoUsuario"]=u
    return render(request, 'submissao.html', data)



def avaliar(request):
    r_cpf=request.session["logado_cpf"]
    data={}
    u=Usuario.objects.get(cpf=r_cpf)
    data["logadoUsuario"]=u
    return render(request, 'avaliar.html', data)



def avaliacao(request):
    r_cpf=request.session["logado_cpf"]
    data={}
    u=Usuario.objects.get(cpf=r_cpf)
    data["logadoUsuario"]=u
    return render(request, 'avaliador.html', data)



def gerencia(request):
    r_cpf=request.session["logado_cpf"]
    data={}
    u=Usuario.objects.get(cpf=r_cpf)
    data["logadoUsuario"]=u
    return render(request, 'gerencia_trabalho.html', data)



def submeter(request):
    r_cpf=request.session["logado_cpf"]
    data={}
    u=Usuario.objects.get(cpf=r_cpf)
    data["logadoUsuario"]=u
    return render(request, 'submeter.html', data)



def gerarCracha(request):
    data={}
    data['participantes']= Participante.objects.all()
    u=Usuario.objects.get(cpf=r_cpf)
    data["logadoUsuario"]=u
    return render(request, 'gerar_cracha.html', data)




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                   PARTE DO ADMIN                          # 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

def deslogarAdmin(request):
    request.session["admin_logado"]=False
    request.session["admin_logado_nome"]=""
    return redirect(loginAdmin)

def loginAdmin(request):
    data={}
    if request.method == 'POST':
        data["retorno"]={}
        p_nome=request.POST.get("nome","")
        existencia=Administrador.objects.filter(nome=p_nome).exists()
        if existencia == True:
            a=Administrador.objects.get(nome=p_nome)
            p_senha=request.POST.get("senha","")
            if a.senha == p_senha:
                request.session["admin_logado_nome"]=p_nome
                request.session["admin_logado"]=True
                return redirect(dashboard)
            else:
                data["retorno"]["nome"]=p_nome
                data["retorno"]["nome_validade"]="is-valid"
                data["retorno"]["senha_mensagem"]="Senha não corresponde!"
                data["retorno"]["senha_validade"]="is-invalid"
                data["retorno"]["senha_feedback"]="invalid-feedback"
                # Retornando pagina
                return render(request, 'admin/loginadmin.html',data)
        else:
            data["retorno"]["nome_mensagem"]="Usuario não encontrado!"
            data["retorno"]["nome_validade"]="is-invalid"
            data["retorno"]["nome_feedback"]="invalid-feedback"
            return render(request, 'admin/loginadmin.html',data)
    else: 
        admins=Administrador.objects.all().count()
        if admins == 0:
            a=Administrador.objects.create(nome="hackathon",senha="ifroconpex")
            a.save()
        if "admin_logado" in request.session:
            if request.session["admin_logado"]==True:
                return redirect(dashboard)    
            else:
                return render(request, 'admin/loginadmin.html',data)
        else:
           return render(request, 'admin/loginadmin.html',data)
    

def dashboard(request):
    data={}
    if "admin_logado" in request.session:
        if request.session["admin_logado"]==True:
            data={"eventoslista":Evento.objects.all()}
            data['nome']=request.session["admin_logado_nome"]
            return render(request, 'admin/dashboard.html',data)
        else:
            # Retornando pagina padrão
            return redirect(loginAdmin)
    else:
        # Retornando pagina de login
        return redirect(loginAdmin)

def departamento(request):
    data={}
    if "admin_logado" in request.session:
        if request.session["admin_logado"]==True:
            data["departamentolista"]=Departamento.objects.all()
            data['nome']=request.session["admin_logado_nome"]
            return render(request, 'admin/departamentos.html',data)
        else:
            # Retornando pagina padrão
            return redirect(loginAdmin)
    else:
        # Retornando pagina de login
        return redirect(loginAdmin)
    

def campus(request):
    if "admin_logado" in request.session:
        if request.session["admin_logado"]==True:
            data={"campuslista":Campus.objects.all()}
            data['nome']=request.session["admin_logado_nome"]
            return render(request, 'admin/campus.html',data)
        else:
            # Retornando pagina padrão
            return redirect(loginAdmin)
    else:
        # Retornando pagina de login
        return redirect(loginAdmin)
    

def servidores(request):
    if "admin_logado" in request.session:
        if request.session["admin_logado"]==True:
            data={"servidoreslista":Servidor.objects.all()}
            data['nome']=request.session["admin_logado_nome"]
            return render(request, 'admin/servidores.html',data)
        else:
            # Retornando pagina padrão
            return redirect(loginAdmin)
    else:
        # Retornando pagina de login
        return redirect(loginAdmin)
    

def novoevento(request):
    data={}
    if "admin_logado" in request.session:
        if request.session["admin_logado"]==True:
            if request.method=="POST":
                form=EventoModelForm(request.POST,request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect(dashboard)
                else:
                    data['erro']='Alguma informação esta invalida!'
                    return render(request, 'admin/novoevento.html',data)
            else:
                data['form']=EventoModelForm()
                data['nome']=request.session["admin_logado_nome"]
                return render(request, 'admin/novoevento.html',data)
        else:
            # Retornando pagina padrão
            return redirect(loginAdmin)
    else:
        # Retornando pagina de login
        return redirect(loginAdmin)

def novocampus(request):
    data={}
    if "admin_logado" in request.session:
        if request.session["admin_logado"]==True:
            if request.method == 'POST':
                p_nome=request.POST.get("nome","")
                p_numero=request.POST.get("numero","")
                p_cep=request.POST.get("cep","")
                p_logradouro=request.POST.get("logradouro","")
                p_referencia=request.POST.get("referencia","")
                p_bairro=request.POST.get("bairro","")
                p_municipio=request.POST.get("municipio","")
                c=Campus.objects.create(nome=p_nome,numero=p_numero,cep=p_cep,logradouro=p_logradouro,referencia=p_referencia,bairro=p_bairro,municipio=p_municipio)                
                c.save()
                return redirect(campus)
            else:
                data['nome']=request.session["admin_logado_nome"]
                return render(request, 'admin/novocampus.html',data)
        else:
            # Retornando pagina padrão
            return redirect(loginAdmin)
    else:
        # Retornando pagina de login
        return redirect(loginAdmin)

def novodepartamento(request):
    data={}
    if "admin_logado" in request.session:
        if request.session["admin_logado"]==True:
            if request.method == 'POST':
                p_nome=request.POST.get("nome","")
                p_campus=request.POST.get("campus","")
                campus_selected=Campus.objects.get(id=p_campus)                
                d=Departamento.objects.create(nome=p_nome,campus=campus_selected)
                d.save()
                return redirect(departamento)
            else:
                data["quantidade_campus"]=Campus.objects.all().count()
                data["campuslista"]=Campus.objects.all()
                data['nome']=request.session["admin_logado_nome"]
                return render(request, 'admin/novodepartamento.html',data)
        else:
            # Retornando pagina padrão
            return redirect(loginAdmin)
    else:
        # Retornando pagina de login
        return redirect(loginAdmin)

def novoservidor(request):
    data={}
    if "admin_logado" in request.session:
        if request.session["admin_logado"]==True:
            if request.method == 'POST':
                p_ciap=request.POST.get("ciap","")
                p_usuario=request.POST.get("usuario","")
                p_departamento=request.POST.get("departamento","")
                u=Usuario.objects.get(id=p_usuario)
                d=Departamento.objects.get(id=p_departamento)
                s=Servidor.objects.create(ciap=p_ciap,departamento=d,usuario=u)
                s.save()
                return redirect(servidores)
            else:
                data["departamentoquant"]=Departamento.objects.all().count()
                data["usuarioquant"]=Usuario.objects.all().count()
                data["departamento_lista"]=Departamento.objects.all()
                data["usuario_lista"]=Usuario.objects.all()
                data['nome']=request.session["admin_logado_nome"]
                return render(request, 'admin/novoservidor.html',data)
        else:
            # Retornando pagina padrão
            return redirect(loginAdmin)
    else:
        # Retornando pagina de login
        return redirect(loginAdmin)
