from django.db import models

class Resultado (models.Model):
    id = models.TextField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    respuesta=models.TextField()
# Create your models here.

def __str__(self):
        return self.id
