from django.urls import path
from .views import listar_resultado, crear_resultado

urlpatterns = [
    path('Resultado/get/Resultado', listar_resultado, name='listar_resultado'),
    path('Resultado/post/Resultado', crear_resultado, name='crear_resultado'),
]
