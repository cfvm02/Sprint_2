from django.urls import path
from .views import medicos_view

urlpatterns = [
    path('', medicos_view, name='medicos_view'),
]
