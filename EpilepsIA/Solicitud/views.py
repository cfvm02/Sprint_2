from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from .rabbit import enviar_a_map_requests, get_channel
from .models import Solicitud
from Medico.models import Medico

@csrf_exempt
def solicitudes_view(request):
    if request.method == "GET":
        solicitudes = Solicitud.objects.all()
        solicitudes_list = [
            {
                "id": s.id,
                "fecha": s.fecha,
                "estado": s.estado,
                "examen_id": s.examen.id,
                #"medico": s.medico.id,
            }
            for s in solicitudes
        ]
        return JsonResponse(solicitudes_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        #medico_obj = None
        #medico_id = data.get("medico")
        #f medico_id:
        #    try:
        #        medico_obj = Medico.objects.get(id=medico_id)
        #    except Medico.DoesNotExist:
        #        return JsonResponse({"error": "Medico no encontrado"}, status=404)
        solicitud = Solicitud.objects.create(
            id=data.get("id"),
            fecha=data.get("fecha"),
            estado=data.get("estado"),
            examen_id=data.get("examen_id"),
            #medico=medico_obj
        )
        get_channel()
        enviar_a_map_requests({
        "id_paciente":"34",
        "id_examen": Solicitud.examen.id if Solicitud.examen else None,
        "ubicacion":Solicitud.examen.urlAcceso if Solicitud.examen else None,
        })
        return JsonResponse({
            "id": solicitud.id,
            "fecha": solicitud.fecha,
            "estado": solicitud.estado,
            #"medico": solicitud.medico.id if solicitud.medico else None
        }, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
