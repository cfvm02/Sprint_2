from django.shortcuts import render, redirect
from .models import Resultado

# View to list all Resultado objects
def listar_resultado(request):
    resultados = Resultado.objects.all()
    return render(request, 'listar_resultado.html', {'resultados': resultados})

# View to create a new Resultado object
def crear_resultado(request):
    if request.method == "POST":
        # Extract form data
        id_resultado = request.POST.get('id')
        respuesta = request.POST.get('respuesta')

        # Create the Resultado object
        Resultado.objects.create(id=id_resultado, respuesta=respuesta)

        # Redirect to the list view
        return redirect('listar_resultado')
    else:
        # Render the form to create a new Resultado
        return render(request, 'crear_resultado.html')
