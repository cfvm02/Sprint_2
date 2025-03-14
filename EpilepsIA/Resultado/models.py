import uuid
from django.db import models

from Examen.models import Examen

class Resultado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    respuesta = models.TextField()
    examen = models.OneToOneField(Examen, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
