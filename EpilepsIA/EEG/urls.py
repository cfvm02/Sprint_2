from django.urls import path
from .views import eeg_view

urlpatterns = [
    path('', eeg_view, name='eeg_view'),
]
