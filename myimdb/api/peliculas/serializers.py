""" Serializadores de los endpoints de peliculas """
from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
)

from Rodajes.models import Genero, Pelicula
from Personas.models import Pais, Persona, Tipo


class PersonasPeliculaSerializer(ModelSerializer):
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
class PersonasPeliculaSerializerMin(ModelSerializer):
    """ serializadores de personas minimizado """
    class Meta:
        """Meta"""
        model = Persona
        fields = (
            'nombre',
            'apellido'
        )
class PeliculaSerializer(ModelSerializer):
    """ serializadores de peliculas """
    elenco = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    director = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    guionista = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    generos = SlugRelatedField(
        slug_field='nombre',
        queryset=Genero.objects.all(),        
        many=True,
        required=False,
    )
    class Meta:
        """Meta"""
        model = Pelicula
        fields = (
            'nombre',
            'slug',
            'duracion',
            'puntuacion',
            'elenco',
            'director',
            'guionista',
            'generos'
        )

class PeliculaSerializerWrite(ModelSerializer):
    """ serializadores de peliculas """

    def create(self, validated_data):
        """
        Crear una pelicula
        """
        if 'elenco' in validated_data:
            actores = validated_data.pop('elenco')
        else:
            actores = []

        if 'director' in validated_data:
            directores = validated_data.pop('director')
        else:
            directores = []
        
        if 'generos' in validated_data:
            generos = validated_data.pop('generos')
        else:
            generos = []

        pelicula = Pelicula(**validated_data)
        pelicula.save()

        for actor in actores:
            tipo = actor.pop('tipo')
            persona_actor = Persona.objects.create(
                **actor
            )
            persona_actor.tipo.set(tipo)
            pelicula.elenco.add(persona_actor)

        for director in directores:
            tipo = director.pop('tipo')
            persona_director = Persona.objects.create(
                **director
            )
            persona_director.tipo.set(tipo)
            pelicula.director.add(persona_director)

        pelicula.generos.set(generos)

        return pelicula
    elenco = PersonasPeliculaSerializer(
        many=True,
        required=False
    )
    director = PersonasPeliculaSerializer(
        many=True,
        required=False
    )
    guionista = PersonasPeliculaSerializer(
        many=True,
        required=False
    )
    generos = SlugRelatedField(
        slug_field='nombre',
        queryset=Genero.objects.all(),        
        many=True,
        required=False,
    )
    class Meta:
        """Meta"""
        model = Pelicula
        fields = (
            'nombre',
            'duracion',
            'puntuacion',
            'elenco',
            'director',
            'guionista',
            'generos'
        )