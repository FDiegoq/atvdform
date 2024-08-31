from django.shortcuts import render
from .models import *
from .form import *
# Create your views here.

def index(request):
    alunos=Aluno.objects.all()
    if request.method=='POST':
        form=AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            form=AlunoForm()
    else:
        form=AlunoForm()

    return render(request, 'index.html', {'alunos':alunos, 'form':form})
