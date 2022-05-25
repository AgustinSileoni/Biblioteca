from enum import auto
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from .models import Autor

from .forms import AutorForm

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def crearAutor(request):
    print(request.POST)
    if request.method == 'POST':  #Si el metodo utilizado es post
        autor_form = AutorForm(request.POST)
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
        else:
            autor_form = AutorForm()
    return render(request, 'libro/crear_autor.html',{'autor_form':autor_form})

def listarAutor(request):
    autores = Autor.objects.filter(estado = True)
    return render(request, 'libro/listar_autor.html',{'autores':autores})
	
def editarAutor(request,id):
    autor_form= None
    error = None
    try: 
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance = autor)
        else:
            autor_form = AutorForm(request.POST, instance = autor)
            if autor_form.is_valid():
                    autor_form.save()
            redirect('index')
    except ObjectDoesNotExist as e:
        error = e

    return render(request,'libro/crear_autor.html',{'autor_form':autor_form,'error':error})

def eliminarAutorDirecto(request,id):
	autor= Autor.objects.get(id=id)
	if request.method == 'POST':
		autor.delete()
		return redirect('libro:listar_autor')	
	return render (request, 'libro/eliminar_autor_directo.html',{'autor':autor})

def eliminarAutorLogico(request,id):
    autor = Autor.objects.get(id = id)
    if request.method == 'POST':
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')	
    return render (request, 'libro/eliminar_autor_logico.html',{'autor':autor})