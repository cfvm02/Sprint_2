from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Paciente

@csrf_exempt
def pacientes_view(request):
    if request.method == "GET":
        pacientes = Paciente.objects.all()
        pacientes_list = []
        for p in pacientes:
            pacientes_list.append({
                "id": p.id,
                "nombre": p.nombre,
                "edad": p.edad,
                "medico": p.medico.id if p.medico else None,
                "eventos": [e.id for e in p.eventos.all()]
            })
        return JsonResponse(pacientes_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        # Manejo del médico (si se envía su id)
        medico_obj = None
        medico_id = data.get("medico")
        if medico_id:
            from Medico.models import Medico
            try:
                medico_obj = Medico.objects.get(id=medico_id)
            except Medico.DoesNotExist:
                return JsonResponse({"error": "Medico no encontrado"}, status=404)
        paciente = Paciente.objects.create(
            id=data.get("id"),
            nombre=data.get("nombre"),
            edad=data.get("edad"),
            medico=medico_obj
        )
        # Asignar eventos si se proporcionan
        eventos_ids = data.get("eventos", [])
        if eventos_ids:
            from Evento.models import Evento
            eventos_objs = Evento.objects.filter(id__in=eventos_ids)
            paciente.eventos.set(eventos_objs)
        return JsonResponse({
            "id": paciente.id,
            "nombre": paciente.nombre,
            "edad": paciente.edad,
            "medico": paciente.medico.id if paciente.medico else None,
            "eventos": [e.id for e in paciente.eventos.all()]
        }, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
