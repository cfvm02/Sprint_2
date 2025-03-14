from django.urls import path
from .views import alertas_resultado_view

urlpatterns = [
    path('', alertas_resultado_view, name='alertas_resultado_view'),
]
