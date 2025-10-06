from rest_framework import serializers
from .models import Nacionalidad,Autor,Comuna,Direccion,Biblioteca,Lector,Libro,Prestamo,Genero


class Nacionalidad_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Nacionalidad
# fields = ('fullname','languaje','is_active’) acápodemos traer cualquier atributo o campo del modelo.
        fields = '__all__'
# con la opción '__all__' traemos todos loscampos para ver y tener acceso a todo el registrode cada elemento que pertenezca al modelo

class Autor_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class Comuna_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class Direccion_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class Biblioteca_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Biblioteca
        fields = '__all__'

class Lector_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Lector
        fields = '__all__'

class Libro_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'

class Prestamo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = '__all__'

class Genero_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'