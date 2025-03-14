from .models import Evento

def get_all_eventos():
    eventos = Evento.objects.all()
    return [
        {"id": e.id, "nombre": e.nombre, "edad": e.edad}
        for e in eventos
    ]

def create_evento(data):
    evento = Evento.objects.create(
        id=data.get("id"),
        nombre=data.get("nombre"),
        edad=data.get("edad")
    )
    return {"id": evento.id, "nombre": evento.nombre, "edad": evento.edad}
