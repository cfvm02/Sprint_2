import os
import tempfile
from google.cloud import storage
from django.conf import settings

def upload_blob(source_file_name, destination_blob_name=None):
    """
    Sube un archivo al bucket de Google Cloud Storage usando la configuración definida en settings.py.
    
    :param source_file_name: Ruta local del archivo que deseas subir.
    :param destination_blob_name: Nombre que tendrá el archivo en GCS. Si es None, se usará el nombre local.
    :return: La URL completa del archivo subido.
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

    # Precondición para evitar condiciones de carrera.
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    # Construir la URL pública asumiendo la configuración estándar de GCS
    file_url = f"https://storage.googleapis.com/{bucket_name}/{full_destination}"
    print(f"Archivo {source_file_name} subido a {full_destination} en el bucket {bucket_name}. URL: {file_url}")
    return file_url


def split_edf_file(file_path, parts_count=3):
    """
    Divide un archivo .edf en 'parts_count' partes y guarda cada parte en un archivo temporal.
    
    :param file_path: Ruta del archivo EDF original.
    :param parts_count: Número de partes en que se desea dividir el archivo.
    :return: Lista de rutas de archivos correspondientes a cada parte.
    """
    file_parts = []
    with open(file_path, 'rb') as f:
        data = f.read()

    total_size = len(data)
    part_size = total_size // parts_count

    for i in range(parts_count):
        start = i * part_size
        # En la última parte se agrega todo el remanente
        if i == parts_count - 1:
            part_data = data[start:]
        else:
            part_data = data[start:start+part_size]

        temp_file_path = os.path.join(tempfile.gettempdir(), f"part_{i+1}_{os.path.basename(file_path)}")
        with open(temp_file_path, 'wb') as pf:
            pf.write(part_data)
        file_parts.append(temp_file_path)

    return file_parts
