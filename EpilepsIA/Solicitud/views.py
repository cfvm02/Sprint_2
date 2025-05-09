import json
import uuid
import requests

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from Examen.models import Examen
from .models import Solicitud

API_DESTINO = "http://localhost:5000/enviar"  # Reemplaza con tu URL real

@csrf_exempt
def solicitudes_view(request):
    if request.method == "GET":
        solicitudes = Solicitud.objects.all()
        solicitudes_list = [
            {
                "id": str(s.id),
                "fecha": s.fecha.isoformat(),
                "estado": s.estado,
                "examen_id": str(s.examen.id) if s.examen else None,
            }
            for s in solicitudes
        ]
        return JsonResponse(solicitudes_list, safe=False, status=200)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)

            estado = data.get("estado")
            examen_id = data.get("examen_id")

            if not estado or not examen_id:
                return JsonResponse({"error": "Faltan campos requeridos"}, status=400)

            try:
                examen = Examen.objects.get(id=examen_id)
            except Examen.DoesNotExist:
                return JsonResponse({"error": "Examen no encontrado"}, status=404)

            solicitud = Solicitud.objects.create(
                estado=estado,
                examen=examen
            )

            # Datos que enviaremos a la API externa
            json_para_api = {
                "id_paciente": str(uuid.uuid4()),  # inventado
                "id_examen": str(examen.id),
                "ubicacion_examen": examen.urlAcceso,
            }

            try:
                response = requests.post(API_DESTINO, json=json_para_api)
                response.raise_for_status()
            except requests.RequestException as e:
                return JsonResponse({
                    "error": "Error al enviar a la API externa",
                    "detalle": str(e)
                }, status=502)

            return JsonResponse({
                "id": str(solicitud.id),
                "estado": solicitud.estado,
                "fecha": solicitud.fecha.isoformat(),
                "examen_id": str(examen.id),
                "api_response": response.json() if response.content else {}
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido."}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
