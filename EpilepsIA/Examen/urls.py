from django.urls import path
from .views import ExamenUploadView, examenes_view

urlpatterns = [
    path('', examenes_view, name='examenes_view'),
    path('upload/', ExamenUploadView.as_view(), name='examen_upload'),

]
