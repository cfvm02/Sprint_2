from .models import Paciente

def get_all_pacientes():
    pacientes = Paciente.objects.all()
    result = []
    for p in pacientes:
        result.append({
            "id": p.id,
            "nombre": p.nombre,
            "edad": p.edad,
            "medico": p.medico.id if p.medico else None,
            "eventos": [e.id for e in p.eventos.all()]
        })
    return result

def create_paciente(data):
    # Procesar la relación con Medico si se proporciona
    medico_obj = None
    medico_id = data.get("medico")
    if medico_id:
        from Medico.models import Medico
        try:
            medico_obj = Medico.objects.get(id=medico_id)
        except Medico.DoesNotExist:
            raise Exception("Medico no encontrado")
    paciente = Paciente.objects.create(
        id=data.get("id"),
        nombre=data.get("nombre"),
        edad=data.get("edad"),
        medico=medico_obj
    )
    # Procesar la relación ManyToMany con Evento
    eventos_ids = data.get("eventos", [])
    if eventos_ids:
        from Evento.models import Evento
        eventos_objs = Evento.objects.filter(id__in=eventos_ids)
        paciente.eventos.set(eventos_objs)
    return {
        "id": paciente.id,
        "nombre": paciente.nombre,
        "edad": paciente.edad,
        "medico": paciente.medico.id if paciente.medico else None,
        "eventos": [e.id for e in paciente.eventos.all()]
    }
