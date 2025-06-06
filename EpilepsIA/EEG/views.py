from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import EEG
from django.core.files.storage import default_storage
import requests

@csrf_exempt
def eeg_view(request):
    if request.method == "GET":
        eegs = EEG.objects.all()
        eeg_list = [
            {
                "id": e.id,
                "fecha": e.fecha,
                "solicitud": e.solicitud.id if e.solicitud else None,
                "paciente": e.paciente.id if e.paciente else None,
            }
            for e in eegs
        ]
        return JsonResponse(eeg_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        from Solicitud.models import Solicitud
        from Paciente.models import Paciente
        try:
            solicitud_obj = Solicitud.objects.get(id=data.get("solicitud"))
        except Solicitud.DoesNotExist:
            return JsonResponse({"error": "Solicitud no encontrada"}, status=404)
        try:
            paciente_obj = Paciente.objects.get(id=data.get("paciente"))
        except Paciente.DoesNotExist:
            return JsonResponse({"error": "Paciente no encontrado"}, status=404)
        eeg = EEG.objects.create(
            id=data.get("id"),
            fecha=data.get("fecha"),
            solicitud=solicitud_obj,
            paciente=paciente_obj
        )
        return JsonResponse({
            "id": eeg.id,
            "fecha": eeg.fecha,
            "solicitud": eeg.solicitud.id,
            "paciente": eeg.paciente.id,
        }, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

MAP_URL = "http://10.128.0.2:5000/map"

@csrf_exempt
def subir_eeg(request):
    if request.method == "POST":
        archivo = request.FILES["eeg"]
        ruta_archivo = default_storage.save(archivo.name, archivo)

        # Guardar en la base de datos
        eeg = EEG.objects.create(archivo=ruta_archivo)

        # Enviar el archivo a "map"
        with open(ruta_archivo, "rb") as f:
            response = requests.post(MAP_URL, files={"eeg": f})

        resultado = response.json().get("resultado", "Error")
        eeg.resultado = resultado
        eeg.save()

        return JsonResponse({"mensaje": "EEG procesado", "resultado": resultado})

    return JsonResponse({"error": "Método no permitido"}, status=405)
