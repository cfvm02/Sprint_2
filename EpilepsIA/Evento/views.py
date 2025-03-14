from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Evento

@csrf_exempt
def eventos_view(request):
    if request.method == "GET":
        eventos = Evento.objects.all()
        eventos_list = [
            {"id": e.id, "nombre": e.nombre, "edad": e.edad}
            for e in eventos
        ]
        return JsonResponse(eventos_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        evento = Evento.objects.create(
            id=data.get("id"),
            nombre=data.get("nombre"),
            edad=data.get("edad")
        )
        return JsonResponse(
            {"id": evento.id, "nombre": evento.nombre, "edad": evento.edad},
            status=201
        )
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
