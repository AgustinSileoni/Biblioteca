from unicodedata import name
from django.urls import path

from .views import crearAutor, editarAutor, eliminarAutorDirecto, eliminarAutorDirecto, eliminarAutorLogico,listarAutor


urlpatterns=[
    path('crear_autor/', crearAutor, name = 'crear_autor'),
    path('listar_autor/', listarAutor, name= 'listar_autor'),
    path('editar_autor/<int:id>', editarAutor, name= 'editar_autor'),
    path('eliminar_autor_directo/<int:id>',eliminarAutorDirecto, name='eliminar_autor_directo'),
    path('eliminar_autor_logico/<int:id>',eliminarAutorLogico, name='eliminar_autor_logico'),
    
]