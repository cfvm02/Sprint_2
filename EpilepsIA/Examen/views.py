from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Examen

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ExamenSerializer


@csrf_exempt
def examenes_view(request):
    if request.method == "GET":
        examenes = Examen.objects.all()
        lista = [
            {
                "id": str(e.id),
                "fecha": e.fecha,
                "paciente_id": e.paciente_id,
                "urlAcceso": e.urlAcceso,
                #"solicitud_id": e.solicitud_id,
            }
            for e in examenes
        ]
        return JsonResponse(lista, safe=False, status=200)

    elif request.method == "POST":

        texto = request.POST.get('paciente_id')       # Para campos de texto
        archivo = request.FILES.get('archivo')  # Para archivos
        data={}
        data["paciente_id"] = texto
        data["archivo"] = archivo
        parser_classes = (MultiPartParser, FormParser)
        
        serializer = ExamenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        examen = Examen.objects.create(
            paciente_id=data.get("paciente_id"),
            #solicitud_id=data.get("solicitud_id")
        )

        return JsonResponse({
            "id": str(examen.id),
            "fecha": examen.fecha,
            "paciente_id": examen.paciente_id,
            #"solicitud_id": examen.solicitud_id,
        }, status=201)

    return JsonResponse({"error": "Método no permitido"}, status=405)

class ExamenUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = ExamenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    