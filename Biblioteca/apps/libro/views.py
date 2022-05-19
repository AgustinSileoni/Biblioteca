from enum import auto
from django.shortcuts import redirect, render

from .forms import AutorForm

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def crearAutor(request):
    if request.method == 'POST':
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():   ##
            autor_form.save()   ##Guarda los datos (Propio de form)
            return redirect('index') ##Me redirige a una url
    else:
        autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html',{'autor_form':autor_form})