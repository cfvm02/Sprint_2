from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import AlertaDiagnostico

@csrf_exempt
def alertas_diagnostico_view(request):
    if request.method == "GET":
        alertas = AlertaDiagnostico.objects.all()
        alertas_list = [
            {"id": a.id, "descripcion": a.descripcion, "fecha": a.fecha}
            for a in alertas
        ]
        return JsonResponse(alertas_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        alerta = AlertaDiagnostico.objects.create(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            fecha=data.get("fecha")
        )
        return JsonResponse({
            "id": alerta.id,
            "descripcion": alerta.descripcion,
            "fecha": alerta.fecha,
        }, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
