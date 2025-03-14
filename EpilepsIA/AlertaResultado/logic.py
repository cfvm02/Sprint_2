from .models import AlertaResultado

def get_all_alertas_resultado():
    alertas = AlertaResultado.objects.all()
    return [
        {
            "id": a.id,
            "descripcion": a.descripcion,
            "fecha": a.fecha,
            "alerta_precedente": a.alerta_precedente.id if a.alerta_precedente else None,
            "resultado": a.resultado.id if a.resultado else None,
        }
        for a in alertas
    ]

def create_alerta_resultado(data):
    from AlertaDiagnostico.models import AlertaDiagnostico
    from Resultado.models import Resultado
    alerta_precedente_obj = None
    alerta_precedente_id = data.get("alerta_precedente")
    if alerta_precedente_id:
        try:
            alerta_precedente_obj = AlertaDiagnostico.objects.get(id=alerta_precedente_id)
        except AlertaDiagnostico.DoesNotExist:
            raise Exception("Alerta Diagnostico no encontrada")
    resultado_obj = None
    resultado_id = data.get("resultado")
    if resultado_id:
        try:
            resultado_obj = Resultado.objects.get(id=resultado_id)
        except Resultado.DoesNotExist:
            raise Exception("Resultado no encontrado")
    alerta = AlertaResultado.objects.create(
        id=data.get("id"),
        descripcion=data.get("descripcion"),
        fecha=data.get("fecha"),
        alerta_precedente=alerta_precedente_obj,
        resultado=resultado_obj
    )
    return {
        "id": alerta.id,
        "descripcion": alerta.descripcion,
        "fecha": alerta.fecha,
        "alerta_precedente": alerta.alerta_precedente.id if alerta.alerta_precedente else None,
        "resultado": alerta.resultado.id if alerta.resultado else None,
    }
