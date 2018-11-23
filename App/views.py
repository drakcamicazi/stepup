from django.shortcuts import render, redirect
#from .form import PessoaForm

# Create your views here.
def inicial(request):
    return render(request, 'index.html')
