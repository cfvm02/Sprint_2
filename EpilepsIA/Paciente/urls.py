from django.urls import path
from .views import pacientes_view

urlpatterns = [
    path('', pacientes_view, name='pacientes_view'),
]
