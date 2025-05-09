from django.urls import path
from .views import examenes_view

urlpatterns = [
    path('', examenes_view, name='examenes_view'),
]
