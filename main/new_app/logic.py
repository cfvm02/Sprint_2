from django.shortcuts import get_object_or_404
from .models import Usuario, Paciente, Alerta, Solicitud, Examen, Resultado

# Función auxiliar para obtener un objeto sin lanzar error si es None
def safe_get(model, obj_id):
    return get_object_or_404(model, id=obj_id) if obj_id else None

# Crear un usuario
def crear_usuario(nombre, login, password):
    return Usuario.objects.create(nombre=nombre, login=login, password=password)

# Obtener todos los usuarios
def obtener_usuarios():
    return Usuario.objects.all()

# Crear un paciente
def crear_paciente(nombre, doctor_id=None):
    doctor = safe_get(Usuario, doctor_id)
    return Paciente.objects.create(nombre=nombre, doctor=doctor)

# Obtener todos los pacientes
def obtener_pacientes():
    return Paciente.objects.all()

# Crear una alerta
def crear_alerta(fecha, descripcion, resultado_id, paciente_id):
    resultado = safe_get(Resultado, resultado_id)
    paciente = safe_get(Paciente, paciente_id)
    return Alerta.objects.create(fecha=fecha, descripcion=descripcion, resultado=resultado, paciente=paciente)

# Obtener todas las alertas
def obtener_alertas():
    return Alerta.objects.all()

# Crear una solicitud
def crear_solicitud(fechaInicio, estado, tiempo, examen_id):
    examen = safe_get(Examen, examen_id)
    return Solicitud.objects.create(fechaInicio=fechaInicio, estado=estado, tiempo=tiempo, examen=examen)

# Obtener todas las solicitudes
def obtener_solicitudes():
    return Solicitud.objects.all()

# Crear un examen
def crear_examen(fecha, tipo, urlAcceso, paciente_id):
    paciente = safe_get(Paciente, paciente_id)
    return Examen.objects.create(fecha=fecha, tipo=tipo, urlAcceso=urlAcceso, paciente=paciente)

# Obtener todos los exámenes
def obtener_examenes():
    return Examen.objects.all()

# Crear un resultado
def crear_resultado(fecha, respuesta, examen_id):
    examen = safe_get(Examen, examen_id)
    return Resultado.objects.create(fecha=fecha, respuesta=respuesta, examen=examen)

# Obtener todos los resultados
def obtener_resultados():
    return Resultado.objects.all()

