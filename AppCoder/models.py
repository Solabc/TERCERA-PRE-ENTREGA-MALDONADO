from django.db import models

# Create your models here.
class Grado(models.Model):
    año = models.CharField(max_length=10)
    seccion = models.IntegerField()
    
class Alumno(models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    
class Docente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    cargo= models.CharField(max_length=30)
