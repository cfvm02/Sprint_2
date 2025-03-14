import uuid
from django.db import models

from Solicitud.models import Solicitud
from Paciente.models import Paciente

class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.TextField()
    solicitud = models.OneToOneField(Solicitud, on_delete=models.CASCADE, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.id
