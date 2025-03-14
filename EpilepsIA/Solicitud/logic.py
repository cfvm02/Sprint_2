from .models import Solicitud

def get_all_solicitudes():
    solicitudes = Solicitud.objects.all()
    return [
        {
            "id": s.id,
            "fecha": s.fecha,
            "estado": s.estado,
            "medico": s.medico.id if s.medico else None,
        }
        for s in solicitudes
    ]

def create_solicitud(data):
    from Medico.models import Medico
    medico_obj = None
    medico_id = data.get("medico")
    if medico_id:
        try:
            medico_obj = Medico.objects.get(id=medico_id)
        except Medico.DoesNotExist:
            raise Exception("Medico no encontrado")
    solicitud = Solicitud.objects.create(
        id=data.get("id"),
        fecha=data.get("fecha"),
        estado=data.get("estado"),
        medico=medico_obj
    )
    return {
        "id": solicitud.id,
        "fecha": solicitud.fecha,
        "estado": solicitud.estado,
        "medico": solicitud.medico.id if solicitud.medico else None
    }
