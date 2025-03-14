from django.db import models

from Examen.models import Examen

class MRI(Examen):
    def __str__(self):
        return self.id