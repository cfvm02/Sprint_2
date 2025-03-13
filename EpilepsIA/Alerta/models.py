from django.db import models

class Alerta (models.Model):
# Create your models here.
    id= models.TextField(primary_key=True)
    fecha=models.DateField(auto_created=True)
    descripcion=models.TextField()
def __str__(self):
    return self.id


