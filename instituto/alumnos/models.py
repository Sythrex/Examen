from typing import Any, Dict, Tuple
from django.db import models

# Create your models here.

class AreaCursos(models.Model):
    idArea          = models.AutoField(db_column='idArea', primary_key=True) 
    Descripcion     = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.Descripcion)


class Cursos(models.Model):
    codigo           = models.CharField(primary_key=True, max_length=6, verbose_name='codigo')
    nombre           = models.CharField(max_length=50, verbose_name='nombre')
    sence            = models.CharField(max_length=10, verbose_name='sence')
    #fecha_creacion   = models.DateField(auto_now=False, verbose_name='fecha_creacion') 
    idArea           = models.ForeignKey('AreaCursos',on_delete=models.CASCADE, db_column='idArea', verbose_name='idArea')  
    modalidad        = models.CharField(max_length=30, blank=True, null=True, verbose_name='modalidad')
    objetivo         = models.CharField(max_length=200, blank=True, null=True, verbose_name='objetivo')
    horas            = models.IntegerField(verbose_name='horas')  
    #activo           = models.IntegerField(verbose_name='activoo')
    img              = models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='img')
    
    def __str__(self):
        return str(self.nombre)
    class Meta:      
        ordering = ['nombre']

    def delete(self, using=None, keep_parents=False):
        self.img.storage.delete(self.img.name)
        return super().delete()

