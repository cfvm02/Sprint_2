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
                "id":str(r.id),
                "fecha": r.fecha,
                "respuesta": r.respuesta,
                "examen": str(r.examen) if r.examen else None,
            }
            for r in resultados
        ]
        return JsonResponse(resultados_list, safe=False, status=200)

    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)

        resultado = Resultado.objects.create(
            id=data.get("id"),
            fecha=data.get("fecha"),
            respuesta=data.get("respuesta"),
            examen=data.get("examen")or None  # ahora es UUID directamente
        )

        return JsonResponse({
            "id": resultado.id,
            "fecha": resultado.fecha,
            "respuesta": resultado.respuesta,
            #"examen": str(resultado.examen) if resultado.examen else None,
        }, status=201)

    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)

