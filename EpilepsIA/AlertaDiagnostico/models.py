from django.db import models

from Alerta.models import Alerta

class AlertaDiagnostico(Alerta):
    def __str__(self):
        return self.id
