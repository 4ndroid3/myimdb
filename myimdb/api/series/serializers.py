""" Serializadores de los endpoints de series """
from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User

from Rodajes.models import Capitulo, Serie, Temporada
from Personas.models import Persona


class UserSerializer(ModelSerializer):
    """ serializadores de usuarios """
    class Meta:
        """Meta"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        )

class PersonaSerieSerializer(ModelSerializer):
    """ serializadores de personas """
    usuario = UserSerializer()
    class Meta:
        """Meta"""
        model = Persona
        fields = (
            'usuario',
            'sexo',
            'fecha_nacimiento',
            'debut',
            'pais'
        )

class SeriesSerializer(ModelSerializer):
    """ serializadores de series """

    def create(self, validated_data):
        """
        Crea una serie
        """
        
        actores = validated_data.pop('elenco')
        serie = Serie(**validated_data)
        serie.save()

        for actor in actores:
            user_list = actor.pop('usuario')
            user = User.objects.create(**user_list)
            persona_actor = Persona.objects.create(
                usuario=user,
                **actor
            )
            serie.elenco.add(persona_actor)
    
        return serie

    elenco = PersonaSerieSerializer(many=True)

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

