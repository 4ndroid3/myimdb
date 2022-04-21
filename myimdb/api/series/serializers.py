""" Serializadores de los endpoints de series """
from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    SerializerMethodField,
)
from rest_framework.reverse import reverse

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


class CapituloSerializer(ModelSerializer):
    """ serializadores de capitulos """
    class Meta:
        """Meta"""
        model = Capitulo
        fields = (
            'nombre',
            'numero',
            'duracion',
            'puntuacion',
        )

class TemporadaSerializer(ModelSerializer):
    """ serializadores de temporadas """
    capitulos = CapituloSerializer(many=True)
    cant_capitulos = SerializerMethodField()

    class Meta:
        """Meta"""
        model = Temporada
        fields = (
            'numero',
            'cant_capitulos',
            'capitulos',
        )
    
    def get_cant_capitulos(self, obj):
        """creo un campo nuevo llamado cant_capitulos"""
        return obj.capitulos.count()


class SeriesSerializer(ModelSerializer):
    """ serializadores de series """

    def create(self, validated_data):
        """
        Se re-escribe create para hacer las relaciones many-to-many
        """
        if 'elenco' in validated_data:
            actores = validated_data.pop('elenco')
        else:
            actores = []
        
        if 'creadores' in validated_data:
            creadores = validated_data.pop('creadores')
        else:
            creadores = []
        
        if 'generos' in validated_data:
            generos = validated_data.pop('generos')
        else:
            generos = []
            
        if 'temporadas' in validated_data:
            temporadas = validated_data.pop('temporadas')
        else:
            temporadas = []
        
        serie = Serie(**validated_data)
        serie.save()


        for actor in actores:
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
    temporadas = TemporadaSerializer(
        many=True,
    )
    cant_temporadas = SerializerMethodField()

    class Meta:
        """Meta"""
        model = Serie
        fields = (
            'nombre',
            'elenco',
            'creadores',
            'generos',
            'cant_temporadas',
            'temporadas',
        )

    def get_cant_temporadas(self, obj):
        return obj.temporadas.count()



