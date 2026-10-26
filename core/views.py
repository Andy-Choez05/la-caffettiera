from django.shortcuts import render
from .models import Persona

def home(request):
    # Obtenemos el único registro de Persona (si existe)
    persona = Persona.objects.first()
    return render(request, "core/home.html", {'persona': persona})