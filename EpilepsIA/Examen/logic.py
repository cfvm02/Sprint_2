from .models import Examen

def get_all_examenes():
    examenes = Examen.objects.all()
    return [
        {
            "id": e.id,
            "fecha": e.fecha,
            "solicitud": e.solicitud.id if e.solicitud else None,
            "paciente": e.paciente.id if e.paciente else None,
        }
        for e in examenes
    ]

def create_examen(data):
    from Solicitud.models import Solicitud
    from Paciente.models import Paciente
    #try:
    #    solicitud_obj = Solicitud.objects.get(id=data.get("solicitud"))
    #except Solicitud.DoesNotExist:
    #    raise Exception("Solicitud no encontrada")
    #try:
    #    paciente_obj = Paciente.objects.get(id=data.get("paciente"))
    #except Paciente.DoesNotExist:
    #    raise Exception("Paciente no encontrado")
    examen = Examen.objects.create(
        id=data.get("id"),
        fecha=data.get("fecha"),
        #solicitud=data.get("Solicitud")#solicitud_obj,
        paciente=data.get("paciente"),#paciente_obj,
        link=data.get("link")
    )
    return {
        "id": examen.id,
        "fecha": examen.fecha,
        #"solicitud": examen.solicitud.id,
        "paciente": examen.paciente.id,
    }
