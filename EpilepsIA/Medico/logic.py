from .models import Medico

def get_all_medicos():
    medicos = Medico.objects.all()
    return [
        {"id": m.id, "nombre": m.nombre, "password": m.password}
        for m in medicos
    ]

def create_medico(data):
    medico = Medico.objects.create(
        id=data.get("id"),
        nombre=data.get("nombre"),
        password=data.get("password")
    )
    return {"id": medico.id, "nombre": medico.nombre, "password": medico.password}
