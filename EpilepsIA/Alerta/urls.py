from django.urls import path
from .views import alertas_view

urlpatterns = [
    path('', alertas_view, name='alertas_view'),
]
