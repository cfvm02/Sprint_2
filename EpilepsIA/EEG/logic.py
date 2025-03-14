from .models import EEG

def get_all_eeg():
    eegs = EEG.objects.all()
    return [
        {
            "id": e.id,
            "fecha": e.fecha,
            "solicitud": e.solicitud.id if e.solicitud else None,
            "paciente": e.paciente.id if e.paciente else None,
        }
        for e in eegs
    ]

def create_eeg(data):
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
    eeg = EEG.objects.create(
        id=data.get("id"),
        fecha=data.get("fecha"),
        solicitud=solicitud_obj,
        paciente=paciente_obj
    )
    return {
        "id": eeg.id,
        "fecha": eeg.fecha,
        "solicitud": eeg.solicitud.id,
        "paciente": eeg.paciente.id,
    }
