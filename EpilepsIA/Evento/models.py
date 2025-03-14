import uuid
from django.db import models

class Evento(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha=models.DateField(auto_created=True)
    
    def __str__(self):
        return self.id
