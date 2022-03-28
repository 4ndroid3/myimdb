"""Vistas de series"""

from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from Rodajes.models import Capitulo, Serie, Temporada
from api.series.serializers import CapituloSerializer, PersonaSerieSerializer, SeriesSerializer, TemporadaSerializer
from Personas.models import Persona


class SeriesView(ModelViewSet):
    """ Representación de las Series en la API """
    queryset = Serie.objects.all()
    serializer_class = SeriesSerializer
    lookup_field = 'slug'
    # permission_classes = [permissions.IsAuthenticated]


class TemporadaView(ModelViewSet):
    """ Representación de las Temporadas en la API """
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer
    lookup_field = 'numero'
    # permission_classes = [permissions.IsAuthenticated]

    
class CapituloView(ModelViewSet):
    """ Representación de los Capitulos en la API """
    queryset = Capitulo.objects.all()
    serializer_class = CapituloSerializer
    lookup_field = 'numero'
    # permission_classes = [permissions.IsAuthenticated]

class PersonasSerieView(ModelViewSet):
    """ Representación de las Personas en la API """
    queryset = Persona.objects.all()
    serializer_class = PersonaSerieSerializer
    lookup_field = 'slug'
    # permission_classes = [permissions.IsAuthenticated]
