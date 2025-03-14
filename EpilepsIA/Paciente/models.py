import uuid
from django.db import models

from Evento.models import Evento
from Medico.models import Medico

class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    eventos = models.ManyToManyField(Evento, blank=True)
    medico = models.ForeignKey(Medico, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.id