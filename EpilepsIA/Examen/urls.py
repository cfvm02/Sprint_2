from django.urls import path
from .views import examenes_view

urlpatterns = [
    path('examenes/', examenes_view, name='examenes_view'),
]

