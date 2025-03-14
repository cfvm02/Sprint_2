from django.urls import path
from .views import listar_alerta, crear_alerta, listar_alerta_diagnostico, crear_alerta_diagnostico, listar_alerta_resultado, crear_alerta_resultado

urlpatterns = [
    path('Alerta/get/Alerta', listar_alerta, name='listar_alerta'),
    path('Alerta/post/Alerta', crear_alerta, name='crear_alerta'),
    path('Alerta/get/AlertaDiagnostico', listar_alerta_diagnostico, name='listar_alertaDiagnostico'),
    path('Alerta/post/AlertaDiagnostico', crear_alerta_diagnostico, name='crear_alertaDiagnostico'),
    path('Alerta/get/AlertaResultado', listar_alerta_resultado, name='listar_alertaResultado'),
    path('Alerta/post/AlertaResultado', crear_alerta_resultado, name='crear_alertaResultado'),
]
