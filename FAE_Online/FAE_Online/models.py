from django.db import models

#Creación de modelos

class Usuario(models.Model):
    id = models.models.AutoField(id=True)
    nombreUsuario = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pwd = models.CharField(max_length=45)

