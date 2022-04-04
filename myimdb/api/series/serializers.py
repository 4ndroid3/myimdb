""" Serializadores de los endpoints de series """
from rest_framework.serializers import (
    ModelSerializer,
    SlugRelatedField,
    StringRelatedField,
    HyperlinkedRelatedField,
    RelatedField,
    SerializerMethodField
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

# class CapituloHyperlinkedSerializer(HyperlinkedRelatedField):
#     """ serializadores de capitulos """
#     view_name ='numero'
#     queryset = Capitulo.objects.all()
    
#     def get_url(self, obj, view_name, request, format):
#         print('ACAAAAAAAAAAAAAAAAAAAA')
#         print(obj)
#         url_kwargs = {
#             'series_slug': obj.temporada.serie.slug,
#             'temporadas_numero': obj.temporada.numero,
#         }

#         return reverse(
#             view_name, kwargs=url_kwargs, request=request, format=format
#         )
    
#     def get_object(self, view_name, view_args, view_kwargs):
#         lookup_kwargs = {
#             'series__slug': view_kwargs['series_slug'],
#             'numero': view_kwargs['temporadas_numero'],
#         }
#         return self.get_queryset().get(**lookup_kwargs)


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
        try:
            actores = validated_data.pop('elenco')
        except ValueError:
            actores = []
        try:
            creadores = validated_data.pop('creadores')
        except ValueError:
            creadores = []
        try:
            generos = validated_data.pop('generos')
        except ValueError:
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
            'temporadas_lista'
        )

    def get_cant_temporadas(self, obj):
        return obj.temporadas.count()



