from .models import Alerta

def get_all_alertas():
    alertas = Alerta.objects.all()
    return [
        {
            "id": a.id,
            "descripcion": a.descripcion,
            "fecha": a.fecha,
        }
        for a in alertas
    ]

def create_alerta(data):
    alerta = Alerta.objects.create(
        id=data.get("id"),
        descripcion=data.get("descripcion"),
        fecha=data.get("fecha")
    )
    return {
        "id": alerta.id,
        "descripcion": alerta.descripcion,
        "fecha": alerta.fecha,
    }
