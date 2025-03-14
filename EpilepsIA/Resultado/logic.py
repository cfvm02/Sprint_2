from .models import Resultado

def get_all_resultados():
    resultados = Resultado.objects.all()
    return [
        {
            "id": r.id,
            "fecha": r.fecha,
            "respuesta": r.respuesta,
            "examen": r.examen.id if r.examen else None,
        }
        for r in resultados
    ]

def create_resultado(data):
    from Examen.models import Examen
    examen_obj = None
    examen_id = data.get("examen")
    if examen_id:
        try:
            examen_obj = Examen.objects.get(id=examen_id)
        except Examen.DoesNotExist:
            raise Exception("Examen no encontrado")
    resultado = Resultado.objects.create(
        id=data.get("id"),
        fecha=data.get("fecha"),
        respuesta=data.get("respuesta"),
        examen=examen_obj
    )
    return {
        "id": resultado.id,
        "fecha": resultado.fecha,
        "respuesta": resultado.respuesta,
        "examen": resultado.examen.id if resultado.examen else None,
    }
