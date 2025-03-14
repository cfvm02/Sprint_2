from django.urls import path
from .views import solicitudes_view

urlpatterns = [
    path('', solicitudes_view, name='solicitudes_view'),
]
