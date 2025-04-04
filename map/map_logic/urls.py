from django.urls import path
from .views import examen_create

urlpatterns = [
    path('examen/', examen_create, name='examen_create'),
]
