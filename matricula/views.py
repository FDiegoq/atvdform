from django.shortcuts import render, redirect
from .models import *
from .form import *
# Create your views here.

def index(request):
    alunos=Aluno.objects.all()
    if request.method =='POST':
        form=AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') ##redirecionando para a página novamente para o caso de o navegador enviar o request.POST repetidamente(erro que estava acontecendo)
    else:
        form=AlunoForm()

    return render(request, 'index.html', {'alunos':alunos, 'form':form})
