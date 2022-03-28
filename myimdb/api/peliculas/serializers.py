""" Serializadores de los endpoints de peliculas """
from rest_framework.serializers import ModelSerializer

from Rodajes.models import Pelicula
from Personas.models import Persona

class PeliculaSerializer(ModelSerializer):
    """ serializadores de peliculas """
    class Meta:
        """Meta"""
        model = Pelicula
        fields = '__all__'

class PersonasPeliculaSerializer(ModelSerializer):
    """ serializadores de personas """
    class Meta:
        """Meta"""
        model = Persona
        fields = '__all__'