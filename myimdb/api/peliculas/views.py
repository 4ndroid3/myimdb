"""Vistas de peliculas"""

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from Rodajes.models import Pelicula
from api.peliculas.serializers import PeliculaSerializer, PersonasPeliculaSerializer
from Personas.models import Persona


class PeliculaView(ModelViewSet):
    """ Representación de las Peliculas """
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'


class PersonasPeliculaView(ModelViewSet):
    """ Representación de las Personas en la API """
    queryset = Persona.objects.all()
    serializer_class = PersonasPeliculaSerializer
    lookup_field = 'slug'
    # permission_classes = [permissions.IsAuthenticated]