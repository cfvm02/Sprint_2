from django.shortcuts import render, redirect
from .models import EEG
import json

def crear_eeg(request):
    """
    Vista para crear un examen EEG.
    Si se recibe una petición POST, se extraen los datos del formulario
    y se crea la instancia de EEG. En caso de GET, se muestra el formulario.
    """
    if request.method == "POST":
        # Extraer datos enviados desde el formulario
        id_examen = request.POST.get('id')
        estado = request.POST.get('estado')
        resultado_str = request.POST.get('resultado', None)

        # Si el campo resultado se envía como cadena JSON, se intenta decodificar
        resultado = None
        if resultado_str:
            try:
                resultado = json.loads(resultado_str)
            except json.JSONDecodeError:
                # Si falla la decodificación, se puede manejar el error o dejarlo en None
                resultado = None

        # Crear la instancia de EEG
        EEG.objects.create(id=id_examen, estado=estado, resultado=resultado)

        # Redireccionar a la vista de listado (asegúrate de que el nombre 'listar_eeg' esté configurado en tus urls)
        return redirect('listar_eeg')
    else:
        # Renderizar el formulario para crear un examen EEG
        return render(request, 'crear_eeg.html')


def listar_eeg(request):
    """
    Vista para listar todos los exámenes EEG existentes.
    Recupera todas las instancias de EEG y las envía a la plantilla para su visualización.
    """
    eegs = EEG.objects.all()
    return render(request, 'listar_eeg.html', {'eegs': eegs})

