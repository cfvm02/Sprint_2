from django.db import models

class Examen(models.Model):
    id = models.TextField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.TextField()
    #resultado = models.OneToOneField(Resultado, on_delete=models.CASCADE)
    #solicitud = models.OneToOneField(Solicitud, on_delete=models.CASCADE)
    #paciente = models.ForeginKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id
