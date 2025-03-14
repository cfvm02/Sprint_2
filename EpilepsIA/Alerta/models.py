import uuid
from django.db import models

from Resultado.models import Resultado

class Alerta (models.Model):
# Create your models here.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha=models.DateField(auto_created=True)
    descripcion=models.TextField()
    
    def __str__(self):
        return self.id
    
class AlertaDiagnostico(Alerta):
    descripcion2=models.TextField()
    def __str__(self):
        return self.id

class AlertaResultado(Alerta):
    alerta_precedente = models.ForeignKey(AlertaDiagnostico, on_delete=models.CASCADE, related_name='alertas_resultado')
    resultado = models.OneToOneField(Resultado, on_delete=models.CASCADE)

    def __str__(self):
        return self.id



