from django.db import models

class Examen(models.Model):
    paciente = models.CharField(max_length=255)
    url_acceso = models.URLField()  # URL del archivo original

    def __str__(self):
        return f"{self.paciente} - {self.url_acceso}"


class ExamenParte(models.Model):
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, related_name='partes')
    part_number = models.PositiveIntegerField()
    url_acceso = models.URLField()  # URL del archivo de la parte

    def __str__(self):
        return f"Examen {self.examen.id} - Parte {self.part_number}"
