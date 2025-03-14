from django.urls import path
from .views import mri_view

urlpatterns = [
    path('', mri_view, name='mri_view'),
]
