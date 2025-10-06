
from django.db import models


# Create your models here.
class Comuna(models.Model):
    codigo = models.CharField(max_length= 5, null= False)
    nombre = models.CharField(max_length=50, null= False)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete= models.CASCADE)
    calle = models.CharField(max_length= 100, null= False)
    numero = models.CharField(max_length= 15, null= True)
    departamento = models.CharField(max_length= 15, null= True)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)

class Biblioteca(models.Model):
    nombre_biblioteca = models.CharField(max_length=100, null=False)
    id_direccion = models.ForeignKey(Direccion, on_delete= models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)

class Nacionalidad(models.Model):
    pais = models.CharField(max_length= 250, null= False)
    nacionalidad = models.CharField(max_length= 250, null= False)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)

class Lector(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete= models.CASCADE)
    nombre_lector  = models.CharField(max_length = 250, null= False)
    rut = models.IntegerField(null= False)
    dv = models.CharField(max_length = 1, null= False)
    id_direccion = models.ForeignKey(Direccion, on_delete= models.CASCADE)
    habilitado = models.BooleanField(default= True)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)

class Autor(models.Model):
    nombre_autor = models.CharField(max_length = 250, null= False)
    pseudonimo = models.CharField(max_length= 250, null= True)
    id_nacionalidad = models.ForeignKey(Nacionalidad, on_delete= models.CASCADE, null= True)
    bio = models.TextField(null= True)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)

class Genero(models.Model):
    genero = models.CharField(max_length= 250, null= False)
    descripcion = models.CharField(max_length= 250, null= True)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete= models.CASCADE)
    id_genero = models.ForeignKey(Genero, on_delete= models.CASCADE)
    titulo = models.CharField(max_length= 250, null= False)
    id_autor = models.ForeignKey(Autor, on_delete= models.CASCADE)
    paginas = models.IntegerField(null= False)
    copias = models.IntegerField(null= False)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro, on_delete= models.CASCADE, null= True)
    id_lector = models.ForeignKey(Lector, on_delete= models.CASCADE, null= True)
    fecha_prestamo = models.DateTimeField(auto_now_add= True)
    fecha_devolucion = models.DateField(null= False)
    fecha_entrega = models.DateTimeField(auto_now= True)
    created_at = models.DateTimeField(auto_now= True)
    update_at = models.DateTimeField(auto_now= True)