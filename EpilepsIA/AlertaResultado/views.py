from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import AlertaResultado
from AlertaDiagnostico.models import AlertaDiagnostico

@csrf_exempt
def alertas_resultado_view(request):
    if request.method == "GET":
        alertas = AlertaResultado.objects.all()
        alertas_list = [
            {
                "id": a.id,
                "descripcion": a.descripcion,
                "fecha": a.fecha,
                "alerta_precedente": a.alerta_precedente.id if a.alerta_precedente else None,
                "resultado": a.resultado.id if a.resultado else None,
            }
            for a in alertas
        ]
        return JsonResponse(alertas_list, safe=False, status=200)
    elif request.method == "POST":
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "JSON inválido"}, status=400)
        # Obtener alerta diagnóstica asociada
        alerta_precedente_obj = None
        alerta_precedente_id = data.get("alerta_precedente")
        if alerta_precedente_id:
            try:
                alerta_precedente_obj = AlertaDiagnostico.objects.get(id=alerta_precedente_id)
            except AlertaDiagnostico.DoesNotExist:
                return JsonResponse({"error": "Alerta Diagnostico no encontrada"}, status=404)
        # Obtener resultado asociado
        from Resultado.models import Resultado
        resultado_obj = None
        resultado_id = data.get("resultado")
        if resultado_id:
            try:
                resultado_obj = Resultado.objects.get(id=resultado_id)
            except Resultado.DoesNotExist:
                return JsonResponse({"error": "Resultado no encontrado"}, status=404)
        alerta = AlertaResultado.objects.create(
            id=data.get("id"),
            descripcion=data.get("descripcion"),
            fecha=data.get("fecha"),
            alerta_precedente=alerta_precedente_obj,
            resultado=resultado_obj
        )
        return JsonResponse({
            "id": alerta.id,
            "descripcion": alerta.descripcion,
            "fecha": alerta.fecha,
            "alerta_precedente": alerta.alerta_precedente.id if alerta.alerta_precedente else None,
            "resultado": alerta.resultado.id if alerta.resultado else None,
        }, status=201)
    else:
        return JsonResponse({"error": "Método no permitido"}, status=405)
