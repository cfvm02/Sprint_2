import os
import uuid
from django.db import models
from google.cloud import storage
from .helpers import gcs
from EpilepsIA import settings
class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paciente_id = models.IntegerField(null=True, blank=True)  # ID del paciente como entero
    fecha = models.DateTimeField(auto_now_add=True)
    urlAcceso = models.URLField(blank=True)  # puede quedar vacío hasta que se suba el archivo
    archivo = models.FileField(upload_to='examenes/', null=True, blank=True)
    #link = models.TextField(null=True, blank=True)         # Link opcional

    def __str__(self):
        return str(self.id)
    
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
    # link = models.TextField(null=True, blank=True)  # Link opcional

    def __str__(self):
        return str(self.id)
