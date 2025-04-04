import os
from django.db import models

from django.db import models
import uuid

from google.cloud import storage

from new_app.helpers import gcs
from main import settings

class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=255)
    doctor = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre

class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    tipo = models.CharField(max_length=255)
    urlAcceso = models.URLField(blank=True)  # puede quedar vacío hasta que se suba el archivo
    archivo = models.FileField(upload_to='examenes/', null=True, blank=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"Examen {self.id} - {self.tipo}"

    def save(self, *args, **kwargs):
        """
        Al guardar el examen, si se asignó un archivo se sube a GCS y se guarda la URL pública.
        """
        # Bandera para saber si ya se subió el archivo (evitar ciclos en el guardado)
        subir_archivo = self.archivo and not self.urlAcceso

        # Primero guarda el objeto (esto permite que el FileField tenga la propiedad .path)
        super().save(*args, **kwargs)

        if subir_archivo:
            # Obtén la ruta local del archivo subido
            local_path = self.archivo.path
            # Define el nombre del archivo en GCS (por ejemplo, dentro de una carpeta 'examenes/')
            destination_blob_name = f"examenes/{os.path.basename(local_path)}"

            # Llama a la función que sube el archivo al bucket
            gcs.upload_edf_to_bucket(
                settings.GCS_BUCKET_NAME,
                local_path,
                destination_blob_name
            )

            # Construye la URL pública.
            # Nota: Esto asume que el bucket es público o que has configurado la visibilidad adecuada.
            public_url = f"https://storage.googleapis.com/{settings.GCS_BUCKET_NAME}/{destination_blob_name}"

            # Actualiza el campo urlAcceso y guarda de nuevo el objeto
            self.urlAcceso = public_url
            super().save(update_fields=["urlAcceso"])

class Resultado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    respuesta = models.TextField()
    examen = models.OneToOneField(Examen, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Resultado {self.id} - {self.fecha}"

class Alerta(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    descripcion = models.TextField()
    resultado = models.ForeignKey(Resultado, on_delete=models.CASCADE, null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Alerta {self.id} - {self.fecha}"

class Solicitud(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fechaInicio = models.DateField()
    estado = models.CharField(max_length=50)
    tiempo = models.FloatField()
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Solicitud {self.id} - {self.estado}"



