from django.shortcuts import render, redirect
from .form import PersonaForm
from .models import Persona

# Create your views here.
def ingresar_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_personas')
    else:
        form = PersonaForm()
    return render(request, 'mi_app/ingresar_persona.html', {'form': form})

def ver_personas(request):
    personas = Persona.objects.all()
    return render(request, 'mi_app/ver_personas.html', {'personas': personas})