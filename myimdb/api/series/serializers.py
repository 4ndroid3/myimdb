""" Serializadores de los endpoints de series """
from rest_framework.serializers import ModelSerializer

from Rodajes.models import Capitulo, Serie, Temporada
from Personas.models import Persona

class SeriesSerializer(ModelSerializer):
    """ serializadores de series """
    class Meta:
        """Meta"""
        model = Serie
        fields = '__all__'


class CapituloSerializer(ModelSerializer):
    """ serializadores de capitulos """
    class Meta:
        """Meta"""
        model = Capitulo
        fields = '__all__'


class TemporadaSerializer(ModelSerializer):
    """ serializadores de temporadas """
    class Meta:
        """Meta"""
        model = Temporada
        fields = '__all__'

class PersonaSerieSerializer(ModelSerializer):
    """ serializadores de personas """
    class Meta:
        """Meta"""
        model = Persona
        fields = '__all__'