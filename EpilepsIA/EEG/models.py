from django.db import models

from Examen.models import Examen

class EEG(Examen):
    def __str__(self):
        return self.id
