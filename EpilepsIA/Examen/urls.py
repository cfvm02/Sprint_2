from django.urls import include, path
from django.views.decorators.csrf import csrf_exempt

from .views import listar_eeg, crear_eeg

urlpatterns = [
    #path('Examen/get/miRNA/', ),
    #path('Examen/post/miRNA/', ),
    #path('Examen/get/MRI/', ),
    #path('Examen/post/MRI/', ),
    path('Examen/get/EEG', listar_eeg, name='listar_eeg'),
    path('Examen/post/EEG', crear_eeg, name='crear_eeg'),
]