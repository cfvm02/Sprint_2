from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Examen

@csrf_exempt
def examenes_view(request):
    if request.method == "GET":
        examenes = Examen.objects.all()
        lista = [
            {
                "id": str(e.id),
                "fecha": e.fecha,
                "paciente_id": e.paciente_id,
                "solicitud_id": e.solicitud_id,
            }
            for e in examenes
        ]
        return JsonResponse(lista, safe=False, status=200)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        examen = Examen.objects.create(
            paciente_id=data.get("paciente_id"),
            solicitud_id=data.get("solicitud_id")
        )

        return JsonResponse({
            "id": str(examen.id),
            "fecha": examen.fecha,
            "paciente_id": examen.paciente_id,
            "solicitud_id": examen.solicitud_id,
        }, status=201)

    return JsonResponse({"error": "Método no permitido"}, status=405)
