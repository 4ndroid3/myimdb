""" Serializadores de los endpoints de peliculas """
from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
)

from Rodajes.models import Elenco, Genero, Pelicula
from Personas.models import Pais, Persona, Tipo

class PersonaPeliculaSerializerMinWrite(ModelSerializer):
    """ Serializador de las personas en la pelicula """
    # tipo = SlugRelatedField(
    #     slug_field='nombre',
    #     queryset=Tipo.objects.all(),
    #     required=False,
    #     many=True,
    # )
    class Meta:
        model = Persona
        fields = ('nombre', 'apellido', 'tipo')

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
    class Meta:
        model = Elenco
        fields = (
            'content_object',
            'actores',
            'directores',
            'guionistas'
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
            'año',
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

        # if 'director' in validated_data:
        #     directores = validated_data.pop('director')
        # else:
        #     directores = []
        
        # if 'guionista' in validated_data:
        #     guionistas = validated_data.pop('guionista')
        # else:
        #     guionistas = []
        
        if 'generos' in validated_data:
            generos = validated_data.pop('generos')
        else:
            generos = []

        pelicula = Pelicula(**validated_data)
        pelicula.save()

        elenco = Elenco()

        for actor in actores:
            persona_actor = Persona.objects.get_or_create(**actor)[0] #--> [Persona, True]
            elenco.actores.set(persona_actor)

        # for director in directores:
        #     tipo = director.pop('tipo')
        #     persona_director = Persona.objects.get_or_create(**director)[0] #--> [Persona, True]
        #     persona_director.tipo.add(tipo[0])
        #     pelicula.director.add(persona_director)
        
        # for guionista in guionistas:
        #     tipo = guionista.pop('tipo')
        #     persona_guionista = Persona.objects.get_or_create(**guionista)[0] #--> [Persona, True]
        #     persona_guionista.tipo.add(tipo[0])
        #     pelicula.guionista.add(persona_guionista)

        elenco.save()
        pelicula.elenco.set(elenco)
        pelicula.generos.set(generos)

        return pelicula

    elenco = PersonaPeliculaSerializerMinWrite(
        many=True,
        required=False
    )
    # director = PersonaPeliculaSerializerMinWrite(
    #     many=True,
    #     required=False
    # )
    # guionista = PersonaPeliculaSerializerMinWrite(
    #     many=True,
    #     required=False
    # )
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
            'año',
            'elenco',
            # 'director',
            # 'guionista',
            'generos'
        )