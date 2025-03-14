from django.urls import path
from .views import eventos_view

urlpatterns = [
    path('', eventos_view, name='eventos_view'),
]
