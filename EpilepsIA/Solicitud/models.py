import uuid
from django.db import models

from Medico.models import Medico

class Solicitud(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=255)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='solicitudes')
    
    def __str__(self):
        return str(self.id)