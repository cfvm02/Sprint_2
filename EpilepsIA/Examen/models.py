import uuid
from django.db import models

class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.TextField()
    #resultado = models.OneToOneField(Resultado, on_delete=models.CASCADE)
    #solicitud = models.OneToOneField(Solicitud, on_delete=models.CASCADE)
    #paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id

class miRNA(Examen):
    resultado = models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.id
    
class MRI(Examen):
    resultado = models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.id
    
class EEG(Examen):
    resultado = models.JSONField(null=True, blank=True)
    def __str__(self):
        return self.id