from django.forms.widgets import ClearableFileInput
from django import forms
from .models import Evento,Usuario,Atividade
SEXO=(
    ("Masculino","Masculino"),
    ("Femenino","Femenino")
)
TIPOS= (
    ('Palestra', 'Palestra'),
    ('Oficina', 'Oficina'),
    ('Roda de Conversa', 'Roda de Conversa'),
    ('Mostra', 'Mostra'),
    ('Minicurso', 'Minicurso'),
    ('Competição', 'Competição'),
)

class EventoModelForm(forms.ModelForm):
    banner:forms.ImageField(widget=ClearableFileInput)
    class Meta:
        model= Evento
        fields='__all__'
        widgets={
            'nome':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nome do evento'
            }),
            'campus':forms.Select(),
            'data_inicial':forms.TextInput(attrs={
                'class':'form-control datapick',
                'placeholder':'AAAA-MM-DD'
            }),
            'data_final':forms.TextInput(attrs={
                'class':'form-control datapick',
                'placeholder':'AAAA-MM-DD'
            }),
            'hora_inicial':forms.TextInput(attrs={
                'class':'form-control timepick',
                'placeholder':'HH:mm'
            }),
            'hora_final':forms.TextInput(attrs={
                'class':'form-control timepick',
                'placeholder':'HH:mm'
            }),
            'descricao': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Descrição sobre o evento.',
                'rows':'3'
            }),
            'organizadores':forms.SelectMultiple()
        }

class UsuarioModelForm(forms.ModelForm):
    foto:forms.ImageField(widget=ClearableFileInput)
    class Meta:
        model= Usuario 
        fields=['nome', 'sobrenome','cpf','senha','email','sexo','data', 'foto']
        widgets={
            'nome':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nome',
                'required':"required"
            }),
            'sobrenome':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Sobrenome',
                'required':"required"
            }),
            'sexo':forms.Select(choices=SEXO,attrs={
                'class':'custom-select'
            }),
            'data':forms.TextInput(attrs={
                'class':'form-control datapick',
                'placeholder':'AAAA-MM-DD',
                'required':"required"
            }),
            'cpf':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'000.000.000-00',
                'required':"required"
            }),
            'senha': forms.PasswordInput(attrs={
                'class':'form-control',
                'placeholder':'Senha',
                'required':"required"
            }),
            "email":forms.EmailInput(attrs={
                'class':'form-control',
                'placeholder':'E-mail',
                'required':"required"
            })
        }

class AtividadeModelForm(forms.ModelForm):
    class Meta:
        model=Atividade
        fields=['titulo','local','descricao','tipo','data','hora_inicial','hora_final','responsaveis','evento']
        widgets={
            'titulo':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Nome da atividade',
                'required':"required"
            }),
            'local':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Local onde ocorrerá a atividade',
                'required':"required"
            }),
            'descricao':forms.Textarea(attrs={
                'class':'form-control bg-lighter',
                'rows':6,
                'required':"required"
            }),
            'data':forms.TextInput(attrs={
                'class':'form-control datapick',
                'placeholder':'AAAA-MM-DD',
                'required':"required"
            }),
            'hora_inicial':forms.TextInput(attrs={
                'class':'form-control timepick',
                'placeholder':'HH:mm'
            }),
            'hora_final':forms.TextInput(attrs={
                'class':'form-control timepick',
                'placeholder':'HH:mm'
            }),
            'tipo':forms.Select(choices=TIPOS),
            'evento':forms.Select(attrs={
                'id':'evento'
            }),
            'responsaveis':forms.SelectMultiple()
        }