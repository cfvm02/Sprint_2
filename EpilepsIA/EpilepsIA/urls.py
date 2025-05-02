from django.contrib import admin
from django.urls import path, include

from .views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('evento/', include('Evento.urls')),
    path('medico/', include('Medico.urls')),
    path('paciente/', include('Paciente.urls')),
    path('solicitud/', include('Solicitud.urls')),
    path('examen/', include('Examen.urls')),
    path('resultado/', include('Resultado.urls')),
    path('alerta/', include('Alerta.urls')),
    path('alerta-diagnostico/', include('AlertaDiagnostico.urls')),
    path('alerta-resultado/', include('AlertaResultado.urls')),
    path('mirna/', include('miRNA.urls')),
    path('mri/', include('MRI.urls')),
    path('eeg/', include('EEG.urls')),
    path('health', health_check, name='health'),
]
