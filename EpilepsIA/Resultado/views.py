from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Resultado

@csrf_exempt
def resultados_view(request):
    if request.method == "GET":
        resultados = Resultado.objects.all()
        resultados_list = [
            {
                "id": r.id,
                "fecha": r.fecha,
                "respuesta": r.respuesta,
                "examen": r.examen.id if r.examen else None,
            }
            for r in resultados
        ]
        return JsonResponse(resultados_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        examen_obj = None
        examen_id = data.get("examen")
        if examen_id:
            from Examen.models import Examen
            try:
                examen_obj = Examen.objects.get(id=examen_id)
            except Examen.DoesNotExist:
                return JsonResponse({"error": "Examen no encontrado"}, status=404)
        resultado = Resultado.objects.create(
            id=data.get("id"),
            fecha=data.get("fecha"),
            respuesta=data.get("respuesta"),
            examen=examen_obj
        )
        return JsonResponse({
            "id": resultado.id,
            "fecha": resultado.fecha,
            "respuesta": resultado.respuesta,
            "examen": resultado.examen.id if resultado.examen else None,
        }, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
