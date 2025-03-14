from django.urls import path
from .views import resultados_view

urlpatterns = [
    path('', resultados_view, name='resultados_view'),
]
