from django import forms
from .models import *

class AlunoForm(forms.ModelForm):
    class Meta():
        model=Aluno
        fields='__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': ' w-full px-3 py-2  border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'cpf': forms.TextInput(attrs={'class': ' w-full px-3 py-2  border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'email': forms.TextInput(attrs={'class': ' w-full px-3 py-2  border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'}),
            'matricula': forms.TextInput(attrs={'class': ' w-full px-3 py-2  border border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'})
        }

