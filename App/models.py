from django.db import models
from datetime import date

class Administrador(models.Model):
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    SEXO=(
        ("Masculino","Masculino"),
        ("Femenino","Femenino")
    )
    VERIFICACAO=(
        ('Sim','Sim'),
        ('Não','Não')
    )
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(unique=True, max_length=18)
    senha = models.CharField(max_length=50)
    email = models.EmailField()
    sexo = models.CharField(max_length=10,choices=SEXO)
    data = models.CharField(max_length=10)
    descricao=models.TextField(max_length=300,blank=True)
    verificado=models.CharField(max_length=3,choices=VERIFICACAO,default="Não")
    foto= models.ImageField(upload_to="fotoperfil/",default='fotoperfil/default.png',blank=True)

    def __str__(self):
        return self.nome


class Campus(models.Model):
    nome = models.CharField(max_length=200)
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField()
    cep = models.CharField(max_length=20)
    bairro = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    referencia = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=200)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Servidor(models.Model):
    ciap = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.usuario.nome +' - '+self.ciap

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicial = models.DateField()
    data_final = models.DateField()
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    banner = models.ImageField(upload_to="banners/")
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    organizadores = models.ManyToManyField(Servidor)

    def __str__(self):
        return self.nome
    
    def situacao(self):
        if date.today() > self.data_final :
            return "Encerrado"
        elif self.data_inicial > date.today():
            return "Inscrições abertas"
        else:
            return "Em andamento"

class Atividade(models.Model):
    TIPOS= (
        ('Palestra', 'Palestra'),
        ('Oficina', 'Oficina'),
        ('Roda de Conversa', 'Roda de Conversa'),
        ('Mostra', 'Mostra'),
        ('Minicurso', 'Minicurso'),
        ('Competição', 'Competição'),
    )
    titulo = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=50, choices=TIPOS)
    data = models.DateField()
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    responsaveis = models.ManyToManyField(Usuario)

    def __str__(self):
        return self.titulo


class Participante(models.Model):
    TIPOS = (
        ('1', 'Monitor'),
        ('2', 'Aluno'),
        ('3', 'Convidado'),
        ('4', 'Visitante')
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    atividades = models.ManyToManyField(Atividade, blank=True)

    def __str__(self):
        return self.tipo + ' ' + self.usuario.attname



class Trabalho(models.Model):
    STATUS=(
        (1, 'Em Avaliação'),
        (2, 'Aprovado'),
        (3, 'Não Aprovado')
    )
    titulo = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=150)

    arquivo = models.FileField(upload_to="media/trabalhos/")
    autores = models.ManyToManyField(Participante, related_name='Autor')
    apresentadores = models.ManyToManyField(Participante, related_name='Apresentador')
    status = models.CharField(max_length=50, choices=STATUS)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


class Certificado(models.Model):
    codigo_autenticacao = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    atividade  = models.ForeignKey(Atividade, on_delete=models.CASCADE, null=True, blank=True)
    evento  = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    trabalho  = models.ForeignKey(Trabalho, on_delete=models.CASCADE, null=True, blank=True)

