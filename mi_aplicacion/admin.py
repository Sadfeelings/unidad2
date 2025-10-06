from django.contrib import admin
from .models import Biblioteca as biblio, Nacionalidad as nacion, Lector as lector, Autor as autor,Genero as cat, Libro as texto, Prestamo as prest, Comuna as comun, Direccion as direc

# Register your models here.
admin.site.register(biblio)
admin.site.register(nacion)
admin.site.register(lector)
admin.site.register(autor)
admin.site.register(cat)
admin.site.register(texto)
admin.site.register(prest)
admin.site.register(comun)
admin.site.register(direc)