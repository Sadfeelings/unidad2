from django.urls import path, include
from rest_framework import routers
from mi_aplicacion import views
router = routers.DefaultRouter() # este elementoenrutador permite manejar múltiples rutas.
# esta es la base del conjunto de rutas o la raíz de lasrutas
# acá se manejan las rutas o ENDsPOINTS que puedatener tu API
router.register(r'Nacionalidad', views.Nacionalidad_ViewSet)
router.register(r'Autor', views.Autor_ViewSet)
router.register(r'Comuna', views.Comuna_ViewSet)
router.register(r'Direccion', views.Direccion_ViewSet)
router.register(r'Biblioteca', views.Biblioteca_ViewSet)
router.register(r'Lector', views.Lector_ViewSet)
router.register(r'Libro', views.Libro_ViewSet)
router.register(r'Prestamo', views.Prestamo_ViewSet)
router.register(r'Genero', views.Genero_ViewSet)

# la r permite que no se interprete como un salto delínea o como un escape de carácter
# usamos la r para indicar que no tome los caracterescomo \n o \t que es un salto de línea o una tabulación,es un formato tipo RAW de python.
# 'programmers' es un ENDPOINT
urlpatterns = [
path('', include(router.urls))
# la ruta base va a incluir todos los elementos que tengael router que hemos creado en URLS
# esta es la lista de URLS que maneja ROUTER en suselementos URLS
]