from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, PacienteViewSet, AlertaViewSet, SolicitudViewSet, ExamenViewSet, ResultadoViewSet, ExamenUploadView, ExamenDownloadView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'alertas', AlertaViewSet)
router.register(r'solicitudes', SolicitudViewSet)
router.register(r'examenes', ExamenViewSet)
router.register(r'resultados', ResultadoViewSet)

urlpatterns = [
    path('api/examenes/<uuid:examen_id>/download/', ExamenDownloadView.as_view(), name='examen_download'),
    path('api/examenes/upload/', ExamenUploadView.as_view(), name='examen_upload'),
    path('api/', include(router.urls)),

]
