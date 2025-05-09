import uuid
from django.db import models

from Examen.models import Examen

class Solicitud(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=255)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, related_name='examenes',null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    