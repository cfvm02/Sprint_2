from django.shortcuts import render, redirect
from .models import Alerta, alertaResultado, alertaDiagnostico
import json

# View for creating an Alerta
def crear_alerta(request):
    if request.method == "POST":
        fecha = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')
        Alerta.objects.create(fecha=fecha, descripcion=descripcion)
        return redirect('listar_alerta')
    else:
        return render(request, 'crear_alerta.html')

# View for listing all Alerta objects
def listar_alerta(request):
    alertas = Alerta.objects.all()
    return render(request, 'listar_alerta.html', {'alertas': alertas})

# View for creating AlertaDiagnostico
def crear_alerta_diagnostico(request):
    if request.method == "POST":
        alerta = request.POST.get('alerta')
        diagnostico = request.POST.get('diagnostico')
        alertaDiagnostico.objects.create(alerta=alerta, diagnostico=diagnostico)
        return redirect('listar_alertaDiagnostico')
    else:
        return render(request, 'crear_alerta_diagnostico.html')

# View for listing all AlertaDiagnostico objects
def listar_alerta_diagnostico(request):
    alertas_diagnostico = alertaDiagnostico.objects.all()
    return render(request, 'listar_alerta_diagnostico.html', {'alertas_diagnostico': alertas_diagnostico})

# View for creating AlertaResultado
def crear_alerta_resultado(request):
    if request.method == "POST":
        alerta = request.POST.get('alerta')
        resultado = request.POST.get('resultado')
        alertaResultado.objects.create(alerta=alerta, resultado=resultado)
        return redirect('listar_alertaResultado')
    else:
        return render(request, 'crear_alerta_resultado.html')

# View for listing all AlertaResultado objects
def listar_alerta_resultado(request):
    alertas_resultado = alertaResultado.objects.all()
    return render(request, 'listar_alerta_resultado.html', {'alertas_resultado': alertas_resultado})
