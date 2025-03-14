from .models import AlertaDiagnostico

def get_all_alertas_diagnostico():
    alertas = AlertaDiagnostico.objects.all()
    return [
        {
            "id": a.id,
            "descripcion": a.descripcion,
            "fecha": a.fecha,
        }
        for a in alertas
    ]

def create_alerta_diagnostico(data):
    alerta = AlertaDiagnostico.objects.create(
        id=data.get("id"),
        descripcion=data.get("descripcion"),
        fecha=data.get("fecha")
    )
    return {
        "id": alerta.id,
        "descripcion": alerta.descripcion,
        "fecha": alerta.fecha,
    }
