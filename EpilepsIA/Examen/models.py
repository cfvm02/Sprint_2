import uuid
from django.db import models
from Solicitud.models import Solicitud

class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paciente = models.IntegerField(null=True, blank=True)  # ID del paciente como entero
    fecha = models.DateTimeField(auto_now_add=True)
    link = models.TextField(null=True, blank=True)         # Link opcional

    def __str__(self):
        return str(self.id)
