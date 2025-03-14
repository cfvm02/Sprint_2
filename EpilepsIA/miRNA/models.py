from django.db import models

from Examen.models import Examen

class miRNA(Examen):
    def __str__(self):
        return self.id