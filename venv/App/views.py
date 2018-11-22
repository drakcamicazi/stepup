from django.shortcuts import render, redirect
#from .form import PessoaForm

# Create your views here.
def inicial(request):
    return render(request, 'index.html')

def cadastro(request):
    return render(request, 'cadastro.html')
