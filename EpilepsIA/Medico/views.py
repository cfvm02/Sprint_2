from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Medico

@csrf_exempt
def medicos_view(request):
    if request.method == "GET":
        medicos = Medico.objects.all()
        medicos_list = [
            {"id": m.id, "nombre": m.nombre, "password": m.password}
            for m in medicos
        ]
        return JsonResponse(medicos_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        medico = Medico.objects.create(
            id=data.get("id"),
            nombre=data.get("nombre"),
            password=data.get("password")
        )
        return JsonResponse(
            {"id": medico.id, "nombre": medico.nombre, "password": medico.password},
            status=201
        )
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
