""" Serializadores de los endpoints de peliculas """
from django.forms import CharField
from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    RelatedField
)

from Rodajes.models import Elenco, Genero, Pelicula, Serie
from Personas.models import Pais, Persona, Tipo


class PersonaPeliculaSerializerMinWrite(ModelSerializer):
    """ Serializador de las personas en la pelicula """
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido',)

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

class ElencoSerializerWrite(ModelSerializer):
    """Serializador de Elenco para escritura"""

    def create(self, validated_data):
        return validated_data

    actores = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    directores = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    guionistas = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    class Meta:
        """Meta Para Elenco"""
        model = Elenco
        fields = (
            'actores',
            'directores',
            'guionistas'
        )

class ElencoSerializer(ModelSerializer):
    """Serializador de Elenco para escritura"""
    actores = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    directores = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    guionistas = PersonasPeliculaSerializerMin(
        many=True,
        read_only=True,
    )
    class Meta:
        model = Elenco
        fields = (
            'actores',
            'directores',
            'guionistas'
        )

class PeliculaSerializer(ModelSerializer):
    """ serializadores de peliculas """
    elenco = ElencoSerializer(
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
            'anio',
            'elenco',
            'generos'
        )

class PeliculaSerializerWrite(ModelSerializer):
    """ serializadores de peliculas """

    def create(self, validated_data):
        """
        Crear una pelicula
        """
        if 'actores' in validated_data:
            actores = validated_data.pop('actores')
        else:
            actores = []

        if 'directores' in validated_data:
            directores = validated_data.pop('directores')
        else:
            directores = []
        
        if 'guionistas' in validated_data:
            guionistas = validated_data.pop('guionistas')
        else:
            guionistas = []
        
        
        if 'generos' in validated_data:
            generos = validated_data.pop('generos')
        else:
            generos = []

        pelicula = Pelicula(**validated_data)
        pelicula.save()

        elenco = Elenco.objects.create()

        for actor in actores:
            persona_actor = Persona.objects.get_or_create(**actor)[0] #--> [Persona, True]
            tipo = Tipo.objects.get(nombre='Actor')
            persona_actor.tipo.add(tipo)
            elenco.actores.add(persona_actor)

        for director in directores:
            persona_director = Persona.objects.get_or_create(**director)[0] #--> [Persona, True]
            tipo = Tipo.objects.get(nombre='Director')
            persona_director.tipo.add(tipo)
            elenco.directores.add(persona_director)
        
        for guionista in guionistas:
            persona_guionista = Persona.objects.get_or_create(**guionista)[0] #--> [Persona, True]
            tipo = Tipo.objects.get(nombre='Guionista')
            persona_guionista.tipo.add(tipo)
            elenco.guionistas.add(persona_guionista)

        
        pelicula.elenco = elenco
        pelicula.save()
        pelicula.generos.set(generos)

        return pelicula

    # elenco = ElencoSerializerWrite(
    #     required=False
    # )
    # elenco = SlugRelatedField(
    actores = PersonaPeliculaSerializerMinWrite(
        many=True,
        required=False
    )   
    directores = PersonaPeliculaSerializerMinWrite(
        many=True,
        required=False
    )
    guionistas = PersonaPeliculaSerializerMinWrite(
        many=True,
        required=False
    )
    generos = SlugRelatedField(
        slug_field='nombre',
        queryset=Genero.objects.all(),        
        many=True,
        required=False,
    )
    # generos = SlugRelatedField(
    #     slug_field='pk',
    #     read_only=True,
    #     many=True
    # )
    class Meta:
        """Meta"""
        model = Pelicula
        fields = (
            'nombre',
            'duracion',
            'puntuacion',
            'anio',
            'actores',
            'directores',
            'guionistas',
            'generos'
        )