from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome=models.CharField(max_length=350, blank=False, null=False)
    cpf=models.CharField(max_length=12, blank=False, null=False)
    email=models.EmailField(blank=True, null=True)
    matricula=models.CharField(max_length=6, blank=False, null=False)

    def __str__(self):
        return self.nome
