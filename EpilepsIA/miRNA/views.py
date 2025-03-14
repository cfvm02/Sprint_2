from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import miRNA

@csrf_exempt
def mirna_view(request):
    if request.method == "GET":
        mirnas = miRNA.objects.all()
        mirna_list = [
            {
                "id": m.id,
                "fecha": m.fecha,
                "solicitud": m.solicitud.id if m.solicitud else None,
                "paciente": m.paciente.id if m.paciente else None,
            }
            for m in mirnas
        ]
        return JsonResponse(mirna_list, safe=False, status=200)
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
        mirna = miRNA.objects.create(
            id=data.get("id"),
            fecha=data.get("fecha"),
            solicitud=solicitud_obj,
            paciente=paciente_obj
        )
        return JsonResponse({
            "id": mirna.id,
            "fecha": mirna.fecha,
            "solicitud": mirna.solicitud.id,
            "paciente": mirna.paciente.id,
        }, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
