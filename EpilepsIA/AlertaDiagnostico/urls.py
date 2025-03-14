from django.urls import path
from .views import alertas_diagnostico_view

urlpatterns = [
    path('', alertas_diagnostico_view, name='alertas_diagnostico_view'),
]
