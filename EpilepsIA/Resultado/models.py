import uuid
from django.db import models

class Resultado(models.Model):
    # Using UUIDField for a globally unique identifier
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    respuesta = models.TextField()

    def __str__(self):
        return str(self.id)
