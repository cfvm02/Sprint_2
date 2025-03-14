from django.urls import path
from .views import mirna_view

urlpatterns = [
    path('', mirna_view, name='mirna_view'),
]
