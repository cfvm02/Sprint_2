from google.cloud import storage
from django.conf import settings
import os

def upload_blob(source_file_name, destination_blob_name=None):
    """
    Sube un archivo al bucket de Google Cloud Storage usando la configuración definida en settings.py.
    
    :param source_file_name: Ruta local del archivo que deseas subir.
    :param destination_blob_name: Nombre que tendrá el archivo en GCS. Si es None, se usará el nombre local.
    """
    bucket_name = settings.GCS_BUCKET_NAME
    base_folder = getattr(settings, "GCS_BASE_FOLDER", "")

    # Si no se especifica el destino, se usa el nombre del archivo original
    if not destination_blob_name:
        destination_blob_name = os.path.basename(source_file_name)

    # Combina la carpeta base y el nombre del archivo para formar la ruta completa en el bucket
    full_destination = os.path.join(base_folder, destination_blob_name).replace("\\", "/")

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(full_destination)

    # Precondición para evitar condiciones de carrera. Para objetos nuevos, if_generation_match=0 asegura que el objeto no exista.
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(f"Archivo {source_file_name} subido a {full_destination} en el bucket {bucket_name}.")

from google.cloud import storage

def upload_edf_to_bucket(bucket_name, source_file_path, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    
    blob.upload_from_filename(source_file_path)
    print(f"Archivo {source_file_path} subido como {destination_blob_name}")
