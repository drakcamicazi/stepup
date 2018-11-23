from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(unique=True, max_length=14)
    senha = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Instituicao(models.Model):
    nome = models.CharField(max_length=200)
    local = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Departamento(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicial = models.DateField()
    data_final = models.DateField()
    logotipo = models.ImageField(blank=True)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.PROTECT)
    organizador = models.ManyToManyField(Usuario)
    departamento = models.ManyToManyField(Departamento)
    logradouro = models.CharField(max_length=200, blank=True)
    numero = models.CharField(max_length=6, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    referencia = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nome

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
        ('Aluno', 'Aluno do IFRO'),
        ('Servidor', 'Servidor do IFRO'),
        ('Monitor', 'Monitor'),
        ('Convidado', 'Convidado'),
        ('Visitante', 'Visitante externo')
    )
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    atividades = models.ManyToManyField(Atividade)



class Trabalho(models.Model):
    titulo = models.CharField(max_length=200)
    arquivo = models.FileField()
    autores = models.ManyToManyField(Participante)
    status = models.CharField(max_length=50, choices=((1, 'Em Análise'), (2, 'Aprovado'), (3, 'Reprovado')))
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo


class Certificado(models.Model):
    codigo_autenticacao = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    atividade  = models.ForeignKey(Atividade, on_delete=models.CASCADE, null=True, blank=True)
    evento  = models.ForeignKey(Evento, on_delete=models.CASCADE, null=True, blank=True)
    trabalho  = models.ForeignKey(Trabalho, on_delete=models.CASCADE, null=True, blank=True)

