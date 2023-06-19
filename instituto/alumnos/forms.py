#CREAR CLASES PARA FORMULARIOS
from django.forms import ModelForm
from django import forms
from .models import Cursos

class CursosForm(forms.ModelForm):
    class Meta:
        model = Cursos 
        #fields = ['codigo', 'nombre', 'sence', 'idArea', 
         #         'modalidad', 'objetivo', 'horas', 'img'] 
   
        fields = '__all__' 


