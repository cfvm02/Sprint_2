from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Examen

@csrf_exempt
def examenes_view(request):
    if request.method == "GET":
        examenes = Examen.objects.all()
        examenes_list = [
            {
                "id": e.id,
                "fecha": e.fecha,
                "solicitud": e.solicitud.id if e.solicitud else None,
                "paciente": e.paciente.id if e.paciente else None,
            }
            for e in examenes
        ]
        return JsonResponse(examenes_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        # Obtener la Solicitud y el Paciente asociados
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
        examen = Examen.objects.create(
            id=data.get("id"),
            fecha=data.get("fecha"),
            solicitud=solicitud_obj,
            paciente=paciente_obj
        )
        return JsonResponse({
            "id": examen.id,
            "fecha": examen.fecha,
            "solicitud": examen.solicitud.id,
            "paciente": examen.paciente.id,
        }, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
