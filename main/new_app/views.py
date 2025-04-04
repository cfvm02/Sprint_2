from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Usuario, Paciente, Alerta, Solicitud, Examen, Resultado
from .serializers import UsuarioSerializer, PacienteSerializer, AlertaSerializer, SolicitudSerializer, ExamenSerializer, ResultadoSerializer



# Vistas con ViewSets (CRUD automático)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    serializer_class = AlertaSerializer

class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class ExamenViewSet(viewsets.ModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

class ExamenUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ExamenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
import datetime
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Examen
from django.conf import settings
from google.cloud import storage

class ExamenDownloadView(APIView):
    """
    Vista que genera una URL firmada para acceder al archivo del examen en GCS.
    """
    def get(self, request, examen_id):
        examen = get_object_or_404(Examen, id=examen_id)
        if not examen.urlAcceso:
            return Response({"error": "El examen no tiene archivo asociado."}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtén el nombre del bucket desde settings
        bucket_name = settings.GCS_BUCKET_NAME

        # Extrae el nombre del blob (archivo) de la URL guardada.
        # Se asume que la URL tiene el formato: 
        # https://storage.googleapis.com/<bucket>/<ruta_del_blob>
        try:
            blob_name = examen.urlAcceso.split(f"https://storage.googleapis.com/{bucket_name}/")[-1]
        except Exception as e:
            return Response({"error": "Error al parsear la URL del archivo."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Inicializa el cliente de GCS y obtiene el blob
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(blob_name)

        # Genera una URL firmada válida por 1 hora (3600 segundos)
        try:
            signed_url = blob.generate_signed_url(
                expiration=datetime.timedelta(hours=1),
                method="GET"
            )
        except Exception as e:
            return Response({"error": "No se pudo generar la URL firmada.", "detalle": str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Redirige al usuario a la URL firmada para que pueda descargar el archivo
        return redirect(signed_url)
