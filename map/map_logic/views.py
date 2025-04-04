import os
import tempfile
import requests
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Examen, ExamenParte
from .serializers import ExamenSerializer
from .helpers import gcs

@api_view(['POST'])
def examen_create(request):
    serializer = ExamenSerializer(data=request.data)
    if serializer.is_valid():
        examen = serializer.save()
        original_url = examen.url_acceso

        # Descarga del archivo .edf desde la URL proporcionada
        try:
            response = requests.get(original_url)
            response.raise_for_status()
        except Exception as e:
            return Response({'error': f'Error al descargar el archivo: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        # Guarda el archivo en un archivo temporal
        temp_dir = tempfile.gettempdir()
        original_filename = os.path.basename(original_url)
        temp_file_path = os.path.join(temp_dir, original_filename)
        with open(temp_file_path, 'wb') as f:
            f.write(response.content)

        # Se puede optar por subir el archivo original si se desea; en este ejemplo lo dejamos opcional:
        # original_file_url = upload_blob(temp_file_path)

        # Llamada a la función que divide el archivo EDF en partes.
        # Aquí se utiliza un número fijo de partes (ej. 3); se puede parametrizar según se requiera.
        try:
            partes_paths = gcs.split_edf_file(temp_file_path, parts_count=3)
        except Exception as e:
            return Response({'error': f'Error al dividir el archivo: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Procesa cada parte: subirla al bucket, guardar URL y llamar a la API
        for idx, part_path in enumerate(partes_paths, start=1):
            # Define el nombre de destino para la parte, por ejemplo:
            destination_blob_name = f"examen_{examen.id}/parte_{idx}_{original_filename}"
            try:
                part_url = gcs.upload_blob(part_path, destination_blob_name)
            except Exception as e:
                return Response({'error': f'Error al subir la parte {idx}: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            # Crea el registro de la parte en la base de datos
            ExamenParte.objects.create(
                examen=examen,
                part_number=idx,
                url_acceso=part_url
            )
            
            # Llamado a una API externa para cada parte (PANA RABBIT)
            # api_response = requests.post("https://api.ejemplo.com/procesar", json={"examen_id": examen.id, "parte": idx, "url": part_url})
            # print(f"API response for part {idx}: {api_response.json()}")

            # Elimina el archivo temporal de la parte
            os.remove(part_path)

        # Elimina el archivo temporal original
        os.remove(temp_file_path)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
