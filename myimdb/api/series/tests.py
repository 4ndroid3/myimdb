import pytest
from django.contrib.auth.models import User
from random import randint, uniform
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from faker import Faker

from Rodajes.models import Serie

# @pytest.mark.django_db
# def test_create_serie():
#     """prueba"""
#     me = User.objects.get(username='andres')
#     assert me.is_superuser


class SeriesTests(APITestCase):
    """
    tests de series
    """
    fake = Faker('es_MX')
    
    def test_create_serie(self):
        """
        Asegura que puedo crear una serie.
        """
        url = reverse('series-list')
        data = {
            "nombre": "casados con hijos",
            "elenco": [
                {
                    "nombre": "juan",
                    "apellido": "perez",
                    "fecha_nacimiento": "1990-01-01",
                    "debut": "2000-01-01",
                    # "pais": 'argentina',
                    "sexo": "H",
                    # "tipo": [
                    #     "Actor",
                    # ]
                },
            ],
            "creadores": [
                {
                    "nombre": "juan2",
                    "apellido": "perez2",
                    "fecha_nacimiento": "1990-01-01",
                    "debut": "2000-01-01",
                    # "pais": 'argentina',
                    "sexo": "H",
                    # "tipo": [
                    #     "Actor",
                    # ]
                },
            ],
            "generos": [
                
            ]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Serie.objects.count(), 1)
