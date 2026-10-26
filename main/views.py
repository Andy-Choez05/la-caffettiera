from django.shortcuts import render
from core.models import Persona # Importamos el modelo creado

def home(request):
    # Obtenemos el único registro de Persona
    persona = Persona.objects.first()
    return render(request, "index.html", {'persona': persona}) # <-- Quitamos "main/"

def about(request):
    persona = Persona.objects.first()
    return render(request, "about.html", {'persona': persona}) # <-- Quitamos "main/"

def store(request):
    return render(request, "store.html") # <-- Quitamos "main/"

def contact(request):
    return render(request, "contact.html") # <-- Quitamos "main/"

def blog(request):
    return render(request, "blog.html") # <-- Quitamos "main/"

def sample(request):
    return render(request, "sample.html") # <-- Quitamos "main/"