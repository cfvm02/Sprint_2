import uuid
from django.db import models
class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paciente_id = models.IntegerField(null=True, blank=True)  # ID del paciente como entero
    fecha = models.DateTimeField(auto_now_add=True)
    urlAcceso = models.URLField(blank=True)  # puede quedar vacío hasta que se suba el archivo
    archivo = models.FileField(upload_to='examenes/', null=True, blank=True)
    # link = models.TextField(null=True, blank=True)  # Link opcional

    def __str__(self):
        return str(self.id)