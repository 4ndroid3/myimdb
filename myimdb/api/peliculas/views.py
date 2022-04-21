"""Vistas de peliculas"""

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from Rodajes.models import Pelicula
from api.peliculas.serializers import (
    PeliculaSerializer,
    PeliculaSerializerWrite,
    PersonasPeliculaSerializer
)
from Personas.models import Persona


class PeliculaView(ModelViewSet):
    """ Representación de las Peliculas """
    queryset = Pelicula.objects.all().order_by('-id')
    serializer_class = PeliculaSerializer
    serializer_action_classes = {
        'create': PeliculaSerializerWrite,
    }
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'slug'

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()


class PersonasPeliculaView(ModelViewSet):
    """ Representación de las Personas en la API """
    queryset = Persona.objects.all()
    serializer_class = PersonasPeliculaSerializer
    lookup_field = 'slugname'
    # permission_classes = [permissions.IsAuthenticated]