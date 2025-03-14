import uuid
from django.db import models

class Alerta (models.Model):
# Create your models here.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha=models.DateField(auto_created=True)
    descripcion=models.TextField()\
    
    def __str__(self):
        return self.id
    


class alertaResultado(Alerta):
    resultado = models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.id
    
class alertaDiagnostico(Alerta):
    diagnostico = models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.id





