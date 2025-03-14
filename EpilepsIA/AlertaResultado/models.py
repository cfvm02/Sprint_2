from django.db import models

from Alerta.models import Alerta
from AlertaDiagnostico.models import AlertaDiagnostico
from Resultado.models import Resultado

class AlertaResultado(Alerta):
    alerta_precedente = models.ForeignKey(AlertaDiagnostico, on_delete=models.CASCADE, related_name='alertas_resultado')
    resultado = models.OneToOneField(Resultado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id