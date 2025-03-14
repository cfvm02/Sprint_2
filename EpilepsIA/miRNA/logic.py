from .models import miRNA

def get_all_mirna():
    mirnas = miRNA.objects.all()
    return [
        {
            "id": m.id,
            "fecha": m.fecha,
            "solicitud": m.solicitud.id if m.solicitud else None,
            "paciente": m.paciente.id if m.paciente else None,
        }
        for m in mirnas
    ]

def create_mirna(data):
    from Solicitud.models import Solicitud
    from Paciente.models import Paciente
    try:
        solicitud_obj = Solicitud.objects.get(id=data.get("solicitud"))
    except Solicitud.DoesNotExist:
        raise Exception("Solicitud no encontrada")
    try:
        paciente_obj = Paciente.objects.get(id=data.get("paciente"))
    except Paciente.DoesNotExist:
        raise Exception("Paciente no encontrado")
    mirna = miRNA.objects.create(
        id=data.get("id"),
        fecha=data.get("fecha"),
        solicitud=solicitud_obj,
        paciente=paciente_obj
    )
    return {
        "id": mirna.id,
        "fecha": mirna.fecha,
        "solicitud": mirna.solicitud.id,
        "paciente": mirna.paciente.id,
    }
