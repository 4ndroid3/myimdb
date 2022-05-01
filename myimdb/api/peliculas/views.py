"""Vistas de peliculas"""

import traceback
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.response import Response

from Rodajes.models import Pelicula
from api.peliculas.serializers import (
    PeliculaSerializer,
    PeliculaSerializerWrite,
    PersonasPeliculaSerializer,
    PersonaPeliculaSerializerMinWrite
)
from Personas.models import Persona
from rest_framework.renderers import JSONRenderer


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
        """
        Se re-escribe para poder usar varios serializers.
        """
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # print('VALIDATED DATA' ,serializer.validated_data)
        # print('VALIDATED DATA + ELENCO' ,serializer.validated_data['elenco'])

        # for persona in serializer.validated_data['elenco']:
        #     existe_persona = Persona.objects.filter(nombre=persona['nombre'], apellido=persona['apellido']).exists()

            

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}
    

class PersonasPeliculaView(ModelViewSet):
    """ Representación de las Personas en la API """
    queryset = Persona.objects.all()
    serializer_class = PersonasPeliculaSerializer
    serializer_action_classes = {
        'create': PersonaPeliculaSerializerMinWrite,
    }
    lookup_field = 'slugname'
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        """
        Se re-escribe para poder usar varios serializers.
        """
        try:
            return self.serializer_action_classes[self.action]
        except(KeyError, AttributeError):
            return super().get_serializer_class()
