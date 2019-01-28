from django.db import models


class Usuario(models.Model):
    foto= models.ImageField(blank=True)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(unique=True, max_length=14)
    senha = models.CharField(max_length=50)
    email = models.EmailField()
    sexo = models.CharField(max_length=9)
    data = models.DateField()

    def __str__(self):
        return self.nome


class Campus(models.Model):
    nome_fantasia = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18)
    logradouro = models.CharField(max_length=200)
    numero = models.IntegerField(max_length=5)
    bairro = models.CharField(max_length=100)
    referencia = models.CharField(max_length=200)

    def __str__(self):
        return self.nome_fantasia


class Departamento(models.Model):
    nome = models.CharField(max_length=200)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


class Evento(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    data_inicial = models.DateField()
    data_final = models.DateField()
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    banner = models.ImageField(blank=True)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT)
    organizadores = models.ManyToManyField(Usuario)
    departamentos = models.ManyToManyField(Departamento)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    TIPOS= (
        ('1', 'Palestra'),
        ('2', 'Oficina'),
        ('3', 'Roda de Conversa'),
        ('4', 'Mostra'),
        ('5', 'Minicurso'),
        ('6', 'Competição'),
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
        ('1', 'Servidor'),
        ('2', 'Monitor'),
        ('3', 'Aluno'),
        ('4', 'Convidado'),
        ('5', 'Visitante')
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

    arquivo = models.FileField()
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

