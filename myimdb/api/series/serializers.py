""" Serializadores de los endpoints de series """
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from django.contrib.auth.models import User, Group

from Rodajes.models import Capitulo, Genero, Serie, Temporada
from Personas.models import Pais, Persona, Tipo


class PersonaSerieSerializer(ModelSerializer):
    """ serializadores de personas """
    pais = SlugRelatedField(
        slug_field='id',
        queryset=Pais.objects.all(),
        required=False,
    )
    tipo = SlugRelatedField(
        slug_field='nombre',
        queryset=Tipo.objects.all(),
        required=False,
        many=True,
    )
    
    class Meta:
        """Meta"""
        model = Persona
        fields = (
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'debut',
            'pais',
            'sexo',
            'tipo',
        )

class GenerosSerializer(ModelSerializer):
    """ serializadores de generos """
    class Meta:
        """Meta"""
        model = Genero
        fields = '__all__'

class SeriesSerializer(ModelSerializer):
    """ serializadores de series """

    def create(self, validated_data):
        """
        Crea una serie
        """
        try:
            actores = validated_data.pop('elenco')
        except:
            actores = []
        try:
            creadores = validated_data.pop('creadores')
        except:
            creadores = []
        try:
            generos = validated_data.pop('generos')
        except:
            generos = []
        serie = Serie(**validated_data)
        serie.save()


        for actor in actores:
            print('actor:', actor)
            tipo = actor.pop('tipo')
            persona_actor = Persona.objects.create(
                **actor
            )
            persona_actor.tipo.set(tipo)
            serie.elenco.add(persona_actor)
        
        for creador in creadores:
            tipo = creador.pop('tipo')
            persona_creador = Persona.objects.create(
                **creador
            )
            persona_creador.tipo.set(tipo)
            serie.creadores.add(persona_creador)
        
        serie.generos.set(generos)
    
        return serie

    elenco = PersonaSerieSerializer(many=True, required=False)
    creadores = PersonaSerieSerializer(many=True, required=False)
    generos = SlugRelatedField(
        slug_field='nombre',
        queryset=Genero.objects.all(),        
        many=True,
        required=False,
    )

    class Meta:
        """Meta"""
        model = Serie
        fields = (
            'nombre',
            'elenco',
            'creadores',
            'generos'
        )


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

